```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros.
    """
    return ''.join(a[i] ^ b[i]) for i in range(len(a))
    """

# Test case 1
test_cases = ['010', '110', '00', '1000', '1001', '0000']
assertEqual(string_xor('010', '110'),'100')

# Test case 2
test_cases = ['0110', '1110', '1010', '000', '1111', '1011']
assertEqual(string_xor('110', '01'),'1110')

# Test case 3
test_cases = ['000', '1111', '00', '0000', '10101', '101010']
assertEqual(string_xor('1000', '0001'),'101010')

# Test case 4
test_cases = ['1010', '1010', '101010', '1010100', '010101', '0101010']
assertEqual(string_xor('101010', '1010'),'101010')

# Test case 5
test_cases = ['001000', '000110', '00000101', '0111100', '0110100']
assertEqual(string_xor('1111', '000'),'1110)
```
The function performs the XOR operation on two strings, which consists of only ones and zeros, and returns the result as a string. It works by using the string comparison and basic mathematical operation.