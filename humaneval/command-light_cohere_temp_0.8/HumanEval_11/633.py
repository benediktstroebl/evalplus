```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    Result: A bitwise string with ones from a and b, and zeros elsewhere
    """
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
# Example test cases
test_cases = [
    ('010', '110'),
    ('100', '0'),
    ('001', '001'),
    ('1010', '0110'),
    # Add more test cases as needed
]
for a, b in test_cases:
    assert string_xor(a, b) == ''.join()
```