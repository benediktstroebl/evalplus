```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two given strings consisting only of 1s and 0s.
    """
    string_xor('010', '110')
    """
    return '100'

#Test cases for function
test_string_xor = [
    ("input": "010", "cases": "110"),
    ("input": "1010", "cases": "0110"),
    ("input":"1100", "cases":"1010"),
    ("input": "1111", "cases": "0000"),
    (None, None),
]

#This function is designed to run the test cases above and check if the results are correct
for case in test_string_xor:
    assert string_xor(case['input'], case['cases']) == case['expected'],
    print("Passed:", case)
```