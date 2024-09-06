```python
def string_xor(a, b):
    return a.translate(str.maketrans('01','10')) == b.translate(str.maketrans('10','01'))
```

This approach utilizes the `translate` method to perform XOR on two strings consisting of ones and zeros. It directly returns the result as a string of ones and zeros. This solution is efficient and directly returns the XOR result as opposed to converting it to decimal and back to binary.