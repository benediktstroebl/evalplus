```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings consisting of only ones.
    return ''.join(a.join(b))
   return ''.join(list(map(str, set(a + b))))

# Example test cases
print(string_xor('010', '110'))  # Expected output: 100
print(string_xor('111', '110'))  # Expected output: 100
print(string_xor('000', '111'))  # Expected output: 11
print(string_xor('111', '000'))  # Expected output: 11
print(string_xor('11', '111'))   # Expected output: 00
```