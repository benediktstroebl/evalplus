```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    return ''.join(a[i] ^ b[i] for i in range(len(a)))
    """
    return ''.join(int(c) ^ int(d) for c,d in zip(a, b))

print(string_xor('010', '110'))  # Expected output: 100
```