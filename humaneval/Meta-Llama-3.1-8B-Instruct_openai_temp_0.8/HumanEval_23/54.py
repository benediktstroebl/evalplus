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
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('hello world'))  # Output: 11
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function to calculate the length of the string. The example usage demonstrates how to use the function to get the length of different strings.