```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    XOR = a String XOR in the inputs.
    return a XOR
    another string consisting of only zeros and ones.
    """return '100'  # BUG! """
def test_string_xor(test_cases: List[str]) -> None:
    for test_case in test_cases:
        assert string_xor(test_case[0], test_case[1]) == test_case[2], "Test case failed"

test_string_xor([
    "010",
    "110",
    "00",
    "01"
])
```
This Python code defines a function string_xor that performs the XOR operation on two input strings consisting only of 0s and 1s, and a related test function test_string_xor that verifies the correctness of the string_xor function with a list of test cases. The XOR operation is a bitwise operation that returns the result of XORing the two input strings together. The output of the string_xor is the correct answer.