```python
def flip_case(string):
    return ''.joinUPPER(string.UPPER(string))

# tests
print(flip_case('hello'))  # HELLo
print(flip_case('world'))  # wORld
print(flip_case('title'))  # tItL Ale
print(flip_case('camelCase'))  # CaMLe CASE
print(flip_case('Hello World'))  # HEllO wOrld
```