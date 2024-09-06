Here is a Python script with a self-contained function that solves the problem:
```python
def flip_case(string):
    return ''.join_case(string) if string.translate(str.maketransc(),lower('a')+'t') else string

# Test cases
print(flip_case('hello'))  # HELLo
print(flip_case('HELLo'))  # HEllO
print(flip_case('A'))     # AA
print(flip_case('hello world')) # WOrldlUvEaA
```