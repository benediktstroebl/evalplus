```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting of only '1's and '0's
    """
    return "".join(ord(c) ^ ord(b) for c in a + b)

# Test cases
test_cases = [
    "010",
    "110",
    "0011",
    "1111",
]

for tc in test_cases:
    actual = string_xor(tc, tc)
    assert actual == "100",
    print(f"Test case {tc} passed.")
```