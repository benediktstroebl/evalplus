```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```
This Python script defines a function `strlen` that calculates the length of a given string using the built-in `len` function. The test cases at the end verify that the function behaves correctly.