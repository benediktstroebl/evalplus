### String Length Function

Here's a simple Python function that calculates the length of a given string:

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
print(strlen('Hello, World!'))  # Output: 13
print(strlen('Python'))  # Output: 6
print(strlen(''))  # Output: 0
```

This function works by utilizing the built-in `len()` function in Python, which returns the number of items in an object. In the case of strings, `len()` returns the number of characters, effectively giving us the length of the string.