```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    >>> string_xor('010', '110')
    '100'
    """
    # Ensure inputs are the same length by padding with zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Perform XOR operation on each character and join the results
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Test cases
print(string_xor('010', '110'))  # Outputs: '100'
print(string_xor('1010', '1100'))  # Outputs: '0110'
print(string_xor('1', '1'))  # Outputs: '0'
print(string_xor('0', '1'))  # Outputs: '1'
```