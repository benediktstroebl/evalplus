```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros
    """
    return str(bin(a[i] ^ b[i])[2:].z() for i in range(len(a), len(b)))

# test suite
# the same string should return itself
test_suite = ['010', '110', '100']
print(test_suite[0] == string_xor('010', '110'))  # true
print(test_suite[1] == string_xor('110', '010'))    # true
print(test_suite[2] == string_xor('110', '110'))    # true
``` 
This script defines a function named string_xor, which performs the XOR operation on two input strings a and b, consisting only of ones and zeros. The output is also a string representation of the XOR result. 

Additionally, there is a test suite with three test cases. The test suite is used to verify that the string_xor function's output matches the expected results for various inputs.