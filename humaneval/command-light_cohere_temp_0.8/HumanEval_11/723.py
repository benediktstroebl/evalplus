Here is a self-contained Python script that solves the problem of performing XOR on two input strings consisting only of single characters:
```python
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of single characters.
    Returns the string_xor('010', '110')
    '100'
    """
    return ''.join(chr((ord(a[i]) ^ ord(b[i]))) for i in range(len(a)))
```

This function uses the XOR operator to perform the operation on each character in the input strings, and the result is then converted back to a string with the corresponding characters.