```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """Perform binary XOR operation on two strings consisting of only '1's and '0's."""
    return "".join([i ^ j for i, j in ('0', '1') for j in b])
for _ in [
    "010", "001", "1010", "0110", "1110",
    "0000", "1011", "1000",
]:
    assert string_xor(_, _) == "100"

```
Do you want me to help you with anything else related to Python programming or with code debugging and troubleshooting?