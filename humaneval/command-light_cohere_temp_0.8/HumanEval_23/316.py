Here's a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string"""
    return len(string)

# Test case 1
assert strlen('') == 0

# Test case 2
assert strlen('abc') == 3
```

The `strlen` function uses the `len()` function, which returns the length of the given string.  The function is well-tested with the provided test cases, which ensure it correctly calculates the length of the given string.