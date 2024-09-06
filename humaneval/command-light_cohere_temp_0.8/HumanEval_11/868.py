Here's a self-contained Python function that performs the string XOR operation for any two input strings consisting of only ones and zeros:
```python
def string_xor(a: str, b: str) -> str:
    """ Performs binary XOR on two input strings consisting of only ones and zeros.
    return ''.join(a ^ b)
```
The function uses the built-in `join()` function, which performs XOR on two binary strings. It returns the'll the will above, the string that results from performing the XOR operation on the two input strings.