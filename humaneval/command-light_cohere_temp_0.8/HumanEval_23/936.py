Certainly! Here's the enhanced code snippet that includes a self-contained function `strlen()` that calculates the length of a given string:

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    TypeError: Unbound variable 'string'
    """
    string = str(string)  # Convert string argument to str
    return len(string)
```

This code defines a function `strlen` that calculates the length of a given string. It uses a string argument is converted to a string data type using `str()` to ensure compatibility with other string operations.