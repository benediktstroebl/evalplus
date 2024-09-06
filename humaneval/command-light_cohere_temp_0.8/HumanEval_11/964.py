```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function performs XOR operation on two strings consisting only of digits 1 and 0.
    """
    string_xor("010", "110")
    # Output: 100
    """
    return "".join([str[i] ^ str[i + 1] for i in range(len(str))])

# Tests
test_suite = [
    ("010", "110", "100"),
    ("000", "100"),
    ("001", "101"),
    ("110", "010"),
    ("0000", "1111"),
    ("00", "0"),
    ("111", "11"),
    ("1010", "1011")
]

for case, expected in test_suite:
    actual = string_xor(*case.
    assert actual == expected,
```

This code provides a function that performs the XOR operation on two input strings with only digits 1 and 0, and provides test cases to ensure the correctness of the function. It also uses the expected output format for test cases, which are strings containing the corresponding XOR results.