```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings.
    a performs string containing only digits 0 and 1
    """
    return a ^ b

# Test cases
test_string_xor = [
    ("010", "110"),
    ("abc", "123"),
    (" Huston Parker", "0001"),
    ("abc", "ABC"),
    ("6789", "4812"),
    ("", " "),
]

for test_case in test_string_xor:
    actual_result = string_xor(*test_case)
    expected_result = test_case[1]
    print(f"Test case: {test_case[0]}, Expected: {expected_result}, Actual: {actual_result}")
```