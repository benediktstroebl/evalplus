```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
assert strlen('') == 0
assert strlen('abc') == 3

# Test with an empty string
empty_string = ''
assert strlen(empty_string) == 0

# Test with a longer string
long_string = 'Hello World!'
assert strlen(long_string) == 12

print("All tests passed.")
```

This script defines the `strlen` function as specified, then tests it with the given unit tests, as well as two additional tests for good measure. The `assert` statements will raise an `AssertionError` if any of the tests fail.