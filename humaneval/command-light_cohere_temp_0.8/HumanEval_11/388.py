```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of digits 1 and 0.
    Input:
    a and b
    perform string XOR and return result
    """
    return ''.join(str(a ^ int(b[i]) for i in range(len(b))))

test_cases = [
    "010",
    "110",
    "0011",
    "1010",
]

for tc, test in enumerate(test_cases, start=1):
    actual = string_xor(*test.code
    print(f"{tc}: {actual}")
```