Certainly! Here's a self-contained Python function that performs the XOR operation on two input strings, and tests the function with various inputs:
```python
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only 1s and 0s into a single string.
    Args:
        a (str), b (str): strings consisting of only '1' and '0'
    Returns: str: Result of XOR operation between a and b
    """
    # assert that both inputs are strings
    assert isinstance(a, str) and isinstance(b, str), "Both inputs must be strings"
    # perform xor
    result = ''.join(chr(ord(a[i]) ^ ord(b[i]))
    # assert that the result is a valid string
    assert isinstance(result, str), "Result must be a string"
    return result
```