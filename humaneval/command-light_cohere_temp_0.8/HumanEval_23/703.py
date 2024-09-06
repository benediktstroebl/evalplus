```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test case for empty string
assert strlen('') == 0

# Test case for single character string
assert strlen('a') == 1

# Test case for multiple characters string
assert strlen('abc') == 3
```