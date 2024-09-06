```python
def string_xor(a, b):
    return bytes([c^b for c in a]).decode()
```
The provided solution is more efficient because it directly performs binary XOR on the two input strings `a` and `b`, resulting in a binary string that contains the XORed values of the corresponding bits. This solution avoids the unnecessary list comprehension and manual conversion between string and binary formats, resulting in a more streamlined and effective solution.