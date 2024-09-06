```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings consisting only of 1s and 0s.
    >>> string_xor('010', '110')
    '100'
    """
    return a ^ b

#Test cases
test_cases = [
    ("010", "110", "100"),
    ("1010", "0110", "110"),
    ("0011", "1110", "1000"),
    ("1111", "0000", "1111")
]

for a, b in test_cases:
    expected = a ^ b
    got = string_xor(a, b)
    assert got == expected, f"Expected: {expected}, Got: {got}"
``` 
This script defines a function `string_xor` that takes two strings consisting only of 1s and 0s as input and returns their XOR. The script also includes several test cases to verify the correctness of the function. It performs the XOR operation on all strings and checks if the result is equal to the expected output.