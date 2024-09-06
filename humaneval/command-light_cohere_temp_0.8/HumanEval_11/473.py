Here's the self-contained Python function that performs the string XOR operation:
```python
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s.
    Return: a and b as separate strings and return the result as a string.
    """
    two strings are passed to the function using the `str` constructor.
    return a string(list('0' + a + '0' + b + '0'))
```

This function performs the XOR operation on the two input strings, which must consist only of the characters '1' and '0', and returns the result as a string.

Please note that the function assumes that the input strings contain only the characters '1' and '0', and may raise an error if the input does not meet this condition.