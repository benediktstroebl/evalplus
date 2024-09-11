```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
try:
    print(strlen(123))  # Expected output: TypeError
except TypeError as e:
    print(e)
```

This script defines a function `strlen` that returns the length of a given string. It first checks if the input is a string. If not, it raises a `TypeError`. Otherwise, it uses the built-in `len` function to return the length of the string. The script also includes test cases to demonstrate the function's behavior.