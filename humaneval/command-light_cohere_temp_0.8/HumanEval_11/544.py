Here's a self-contained Python function that performs the string XOR operation on two inputs:
```python
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting only of '0's and '1's
    """
    return ''.join(c ^ d for c, d in zip(a, b))
```
The function performs the XOR operation on all corresponding characters in a and b, and the result is a single string consisting of the XOR'd characters.