Here's a self-contained Python function that performs the string XOR operation, following the problem statement:
```python
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings with only ones and zeros.
    """
    return "".join(a, b)
```
This function performs the XOR operation on the two input strings a and b, and returns the result as a string. It uses the Python's `join` method to concatenate the strings together.

This code is self-contained, and does not require any external dependencies or modules. It can be easily to be incorporated into a wider program or used directly as-is.