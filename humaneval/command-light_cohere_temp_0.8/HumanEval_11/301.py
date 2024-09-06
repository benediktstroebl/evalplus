```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Function that XORs two strings consisting only of digits 1s and 0s.
    XOR: 101 101
    """
    return a ^ b

def test_string_xor(test_cases: List[str]) -> List[str]:
    return [string_xor(case, case) for case in test_cases]

test_cases =  [
    "010",
    "110",
    "100",
    "111",
    "007",
    "001",
    "000110",
]
print(test_cases)
print('\n'.join(test_string_xor(test_cases)))
``` 
This code defines a function `string_xor` that XORs two input strings containing only digits 1 and 0. The `test_string_xor` function is used to test the `string_xor` function with a series of test cases. 

You can use this code to solve the problem and test it using the provided test cases.