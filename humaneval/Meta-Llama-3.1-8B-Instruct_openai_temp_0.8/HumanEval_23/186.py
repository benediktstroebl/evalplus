```python
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage:
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
print(strlen("Hello World"))  # Output: 11
```

In this script, the `strlen` function uses Python's built-in `len` function to return the length of the input string. The docstring remains the same as provided, and example usage is added to demonstrate how to use the function.