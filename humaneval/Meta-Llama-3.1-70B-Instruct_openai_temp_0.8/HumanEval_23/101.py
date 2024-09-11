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

This Python script defines a function `strlen` that takes a string as input and returns its length. It utilizes the built-in `len` function to calculate the length. Additionally, there are test cases at the end to verify the correctness of the function.