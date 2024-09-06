```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    """
    result = ''
    for char in a + b:
        if char == '0':
            result += '1'
        else:
            result += '0'
    return result
# Example test cases
test_cases = [
    "010", "110", "100"
]

test_results = []
for test_case in test_cases:
    test_results.append(string_xor(test_case, test_case))

if all(test_results == [
    "100"
])::
    pass
else:
    print("Failed")
```