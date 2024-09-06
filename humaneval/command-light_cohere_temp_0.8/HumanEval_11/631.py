```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """Perform binary XOR operation on two input strings consisting of 0s and 1s."""
    return ''.join([x ^ y for i for i, x, y in zip(a, b)])
# Test cases
test_cases = [
    ('010', '110'),
    ('1010', '001'),
    ('000', '111'),
    ('1111', '001'),
]

for a, b in test_cases:
    print(string_xor(a, b))
```
This code defines a function called `string_xor` that performs the XOR operation on two input strings containing only 0s and 1s, and returns the result as a string. It uses the specific input strings, performs the XOR operation in a loop, and returns the result.