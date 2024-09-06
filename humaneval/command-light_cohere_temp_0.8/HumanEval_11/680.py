```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two strings, both consisting of only digits 1 and 0
    :param a: First string
    :param b: Second string
    :return: Their XOR as a string
    """
    return f"{a^b}0"


# Test cases
test_cases = [
    "010", "110", "000",
    "1010", "1111",
]

for test_case in test_cases:
    actual = string_xor(test_case, "0000")
    assert actual == test_case
```