```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage:
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

This script defines a function `strlen` that returns the length of a given string. It uses the built-in Python `len` function to achieve this. The example usage at the end demonstrates how to use the function.