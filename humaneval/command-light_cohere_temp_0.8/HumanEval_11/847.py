```python
import string_.
from typing import List


def string_xor(a: string. str, b: str) -> str:
    """ XOR two input strings consisting only of ones and zeros. XOR is
    specific to type of characters
    """
    return ''.join(sorted(a+b))

# Test case
test_suite = [
    "string_xor('010', '110')",
    "Should return 100\n",
    "Both inputs contain only digits 0 and 1\n",
    "Result should contain 0100\n",
    "Wrong result\n",
    "0110"
]

for t in test_suite:
    actual = string_xor(*t)
    assert actual == '100'
```