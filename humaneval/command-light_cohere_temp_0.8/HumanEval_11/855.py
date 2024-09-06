```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings consisting only of 1s and 0s.
    return ''.join(a.translate(b), strings a binary xor
    b)

#Test case 1
test_case_1 = "010"
test_case_2 = "101"
test_case_3 = "01"

print(string_xor(test_case_1, test_case_2))  # Output should be 100
print(string_xor(test_case_2, test_case_3))  # Output should be 110
print(string_xor(test_case_3, test_case_1))  # Output should be 101

def string_translate(str:
    """ Input string only consisting of 1s and 0s.
    return ''.join(str.translate('00 strings with all ones as '0'))

# Test case 2
test_case_4 = "101010"

print(string_translate(test_case_4))  # Output should be 01010010
```
This Python code consists of a self-contained function called string_xor. It performs binary XOR on a string consisting only of 1s and 0s, and returns the result as a string. The test cases are also defined to check the correctness of the string_xor function.