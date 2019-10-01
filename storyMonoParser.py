import json
import re

FIELD_REGEX = re.compile(r'\S+ (\S+) = ([^\n]+)')


def parse(txt_file):
  lines = txt_file.read().splitlines()
  main_obj = parse_object(lines, 0)[1]
  return main_obj


def parse_object(lines, line_index):
  name = lines[line_index].split()[-1]
  i = line_index + 1

  if lines[i].endswith('Array Array'):
    return (*parse_array(lines, i + 1), name)

  obj = {}
  base_indent = indentation(lines[i])
  while i < len(lines) and (base_indent == indentation(lines[i])):
    current_line = lines[i]

    if '=' in current_line:
      match = FIELD_REGEX.search(current_line)
      if not match or len(match.groups()) < 2:
        print(f"Couldn't parse {current_line}")
        continue
      obj[match.group(1)] = parse_value(match.group(2))
      i += 1
    else:
      i, nested_obj, nested_obj_name = parse_object(lines, i)
      obj[nested_obj_name] = nested_obj

  return i, obj, name


def parse_array(lines, line_index):
  size = int(lines[line_index].split('= ')[-1])
  i = line_index + 1
  arr = []

  if not size:
    return i, arr

  base_indent = indentation(lines[i])
  while i < len(lines) and (base_indent == indentation(lines[i])):
    current_line = lines[i]
    i += 1

    if '=' in current_line:
      value = parse_value(current_line.split('= ')[-1])
      arr.append(value)
    elif current_line[-1] == ']':
      continue
    else:
      i, nested_obj, nested_obj_name = parse_object(lines, i - 1)
      arr.append(nested_obj)

  return i, arr


def parse_value(value):
  if value[-1] == '"':
    return value[1:-1]
  else:
    return int(value)


def indentation(string):
  return len(string) - len(string.lstrip())


def toDict(filename):
  with open(filename, encoding='utf-8') as f:
    return parse(f)


def toJson(filename):
  py_dict = toDict(filename)
  return json.dumps(py_dict, indent=2)
