```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting only of ones and zeros.
    return sum(a ^ b for i, a in enumerate(a)) ^ sum(b ^ a for i, b in enumerate(b))

# Test cases
strings = ['010', '110', '000', '001', '0110', '1111']
expected = ['100', '101', '000', '101', '110', '111']

for act, exp in zip(strings, expected):
    print(f'Input: {act}, Expected: {exp}')
    print(f'Result: {string_xor(act, exp)}')
```