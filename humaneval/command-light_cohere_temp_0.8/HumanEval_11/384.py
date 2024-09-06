```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only '0's and '1's.
    >>> string_xor('010', '110')
    '100'
    """
    return a ^ b

# Test cases
test_cases = [
    ("010", "110"),
    ("0011", "1111"),
    ("000", "111"),
    ("1010", "0110"),
    ("1000", "1111")
]

for i, (a, b) in enumerate(test_cases):
    result = string_xor(a, b)
    if result != test_cases[i]:
        print(f"Test {i+1}: {a} XOR {b} = {result} does not match.")
``` 
This Python code defines a function `string_xor` that performs the XOR operation on two input strings. The function takes two strings a a and b as its parameters and returns the XOR of these strings. The code also includes a list of test cases, which are strings that should be XORed. The output will display the results of the XOR operation for each test case, and will show an error message if the result does not match the expected output.