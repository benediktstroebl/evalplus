```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3
assert strlen('hello world') == 11
assert strlen('  ') == 1
```