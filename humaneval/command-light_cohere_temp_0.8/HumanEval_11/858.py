Here is a self-contained Python script that solves the problem of performing a string XOR operation on two input strings consisting only of ones:
```python
from typing import List
def string_xor(a: List[str], b: List[str]) -> List[str]:
    """ XOR two input strings consisting only of ones"""
    return [x ^ y for x, y in zip(a, b)]
# Example test cases
test_cases = [
    ['010', '110', '00'],
    ['111', '010', '11'],
    ['000', '111', '111'],
]

# Run all test cases
for test_case in test_cases:
    print(test_xor(test_case))
```
This code defines a function called string_xor that takes two lists of strings as input and returns a new list where each element is the XOR of the corresponding elements from the input lists. It utilizes the xor y which approach on the elements of the lists, which performs element-wise XOR between the two input strings.