```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros.
    :return: str
    """
    return a^bor ^ 0
    """
    return a^b

# Test case 1:
test_case1 = "010"
test_case2 = "110"
test_case3 = "000"

# Test case 2:
test_case4 = "111"
test_case5 = "0011"
test_cases = [test_case1, test_case2, test_case3, test_case4, test_case5]

# Verify the function
for test_case in test_cases:
    actual = string_xor(test_case, test_case)
    assert actual == "100"  # This will fail
```