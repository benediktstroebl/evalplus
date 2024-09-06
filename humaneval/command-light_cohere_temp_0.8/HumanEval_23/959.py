```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case for empty string
assert strlen('') == 0

# Test case for single character string
assert strlen('a') == 1

# Test case for multi-character string
assert strlen('abc') == 3
```