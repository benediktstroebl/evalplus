```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s into a single string"""
    return ''.join(chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

# Test cases
test_suite = [
    ('010', '110'),
    ('001', '101'),
    ('0000', '1111'),
    ('111', '000'),
    ('007', '111')
]

for act in test_suite:
    actual = string_xor(act[0], act[1])
    assert actual == act[2]
``` 
This code defines a function called **string_xor** that performs the XOR operation on two input strings, consisting only of ones and zeros, and returns the result as a single string. It uses the test `for` loop with a tuple of test cases to verify the correctness of the function, each time it takes two strings and performs the XOR operation, then compares the result with the expected output from the test case.