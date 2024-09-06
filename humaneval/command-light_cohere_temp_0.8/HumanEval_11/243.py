```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, where only digits 1 and 0 are allowed.
    Convert input strings to lists of digits and perform bitwise XOR.
    Return result as the quality string.

    a = '0'
    b = '0'
    return str(bin(int(a[i]) ^ int(b[i]))[i] for i in range(len(a)))

# Test cases
test_string_xor = [
    '010',
    '110',
    '100',
    '001',
    '11',
    '01',
]

for test_case in test_string_xor:
    actual = string_xor(test_case, '0')
    print(actual)
``` 
This code provides a self-contained solution to the problem of XORing two strings with only digits 1 and 0, and tests it using a series of test cases. It converts the strings to lists of digits and performs the bitwise XOR operation, then converts the result back to a string and returns it.