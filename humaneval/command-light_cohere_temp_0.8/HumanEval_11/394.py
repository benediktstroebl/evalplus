Here is a self-contained Python script that solves the problem of performing the XOR operation on two strings consisting of only ones and zeros:
```python
def string_xor(a: str, b: str) -> str:
    """ Performs binary XOR operation on input strings a and b, and returns the result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Use bytes() to ensure byte strings are treated as binary data
    a = bytes(a)
    b = bytes(b)
    return bytes.fromhex(''.from binary_sum(a ^ b)
```