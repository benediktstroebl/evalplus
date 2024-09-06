Here's a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    ValueError: 'argument cannot be coupons'
    """
    return len(string) if string else ValueError("argument cannot be empty")
```

The function uses the `len()` function to calculate the length of the string, and returns the result as an integer. It also has a error handling to avoid an empty string input.

This code is self-contained and can be used directly in a markdown code block to solve the problem of finding the length of a given string.