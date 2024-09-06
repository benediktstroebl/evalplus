```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    Return: str
    """
    # type assertion for parameters
    assert isinstance(a, str) and isinstance(b, str), "Both a and b must be strings"
    assert len(a) == len(b)
    assert all(c in '01' for c in a) and all(c in '01' for c in b)
    return a ^ b

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "11"),
    ("11", "01"),
    ("1000", "0000"),
]

test_results = []

for test_case in test_cases:
    test_result = string_xor(test_case[0], test_case[1])
    test_results.append(test_case + test_result)

print("Test Results:")
for result in test_results:
    print(result)
```