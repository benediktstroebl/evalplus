```python
def strlen(string: str) -> int:
    """
    Return length of given string

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

In this script, we define a function `strlen` that takes a string as input and returns its length using the built-in `len` function. We then include test cases to verify the function works correctly. 

Note that this implementation passes the provided doctests, which are the tests written in the docstring of the `strlen` function.