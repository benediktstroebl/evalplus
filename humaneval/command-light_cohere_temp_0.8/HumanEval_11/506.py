```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Inputs are two strings a and b consisting only of single characters,
    return the XORed string.

    For the time complexity of: O(1)
    """
    return ''.join(''.join([chr(a ^ b) for a, b in zip(a, b)])

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "01"),
    ("000", "1111"),
    ("1010", "1101"),
    # Add more test cases here
]

for a, b in test_cases:
    assert string_xor(a, b) == '100'
```  This Python code defines a function called `string_xor`, which takes two input strings containing only single characters and returns the XORed string. The function uses the str.join and the nested list comprehension to perform the XOR operation on the input characters and create the result as a string. This code has a optimized time complexity of O(1) for the XOR operation, as the function performs a single character comparison for each input character. The test cases at the time a couple of input strings and asserts that the output of the `string_xor` function matches the expected result for each case.