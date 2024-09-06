```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings.
    :param a string a: a string consisting only of '0' and '1'
    :param b: b string consisting only of '0' and '1'
    :return: the XOR of a and b
    """
    return ''.join(a ^ b)

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "01"),
    ("11", "10"),
    ("000", "000"),
    ("111", "001"),
]

for t in test_cases:
    actual = string_xor(*t)
    assert actual == t[0] ^ t[1], f"Assertion error: {actual} != {t[0]} ^ {t[1]}"
``` 
The above Python script defines a self-contained function `string_xor` that performs the XOR operation on two input strings consisting only of 0s and 1s. 

The function is tested using a series of test cases, and the results are compared with the expected outputs. 
The `assert` statements are used to verify if the actual output matches the expected output for each test case.