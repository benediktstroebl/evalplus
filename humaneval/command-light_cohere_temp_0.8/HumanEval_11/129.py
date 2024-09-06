```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of '0's and '1's.
    : The name of the function is 'string_xor'.
    :param a: the first string to XOR
    :param b: the second string to XOR
    :return: result of XOR operation between the two input strings
    """
    return ''.join(c ^ d for c, d in zip('010110', b))

# test cases
test_cases = [
    "010", "110", "0011", "00001", "1111",
    "00010", "00111", "11001"
]

for act in test_cases:
    print(f"Input: {act}.strip()
    ...
    Output: {string_xor(act, act)}
    ")
```
This code defines a Python function `string_xor` that performs the XOR operation on two input strings consisting only of '0's and '1'. The function returns the result of the XOR operation as a string. It uses the universal lambda function to iterate over each character in both strings and perform the XOR operation on each pair of characters. The test cases provided demonstrate the expected behavior of the function.