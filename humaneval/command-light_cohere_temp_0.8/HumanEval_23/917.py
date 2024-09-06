```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case using the function with empty string
assert strlen('') == 0

# Test case using the function with one character string
assert strlen('abc') == 3

# Test case using the function with multiple characters string
assert strlen('hello world') == 11
```