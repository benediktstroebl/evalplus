```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings.
    a example inputs only consist of the digit '1' or '0'.
    XOR is the only operation that fits that criteria.
    """
    return sum(a[-1:] ^ b[-1:] for a, b in zip(a, b))

test_string = "010110"
test_result = string_xor(test_string, test_string)
assertEqual(test_result, "100")
```