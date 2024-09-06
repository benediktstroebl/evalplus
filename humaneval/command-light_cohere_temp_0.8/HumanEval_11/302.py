```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    return ''.join(a, b)

# Testing function correctness
test_string_xor = [
    '010'.join(str) ^ '110'.should() == '100',
    '01'.join(str) ^ '11'.should() == '00',
    '00'.join(str) ^ '11'.should() == '11',
    '000'.join(str) ^ '01'.should() == '110',
]

# Perform the test suite
test_string_xor
```