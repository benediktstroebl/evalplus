```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Hello World'))  # Output: 11
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. The docstring explains the function's purpose and includes doctests to verify its correctness. The script also includes test cases to demonstrate the function's usage.