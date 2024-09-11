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

# Example usage:
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This script defines a function `strlen` that takes a string as an argument and returns its length using the built-in `len` function in Python. The example usage at the end demonstrates how to use this function with different inputs.