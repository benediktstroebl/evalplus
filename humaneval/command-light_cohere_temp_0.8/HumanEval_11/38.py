```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on inputs and return result also as a string.
    :param a string a, b: str
    :return: str
    """
    return chr(ord("".join([a,b]))

# Test cases
test_cases = [
    ("010", "110"),
    ("111", "010"),
    ("001", "001"),
    ("001", "010"),
    ("1010", "0110"),
    ("1011", "1011"),
]

# Test function
def test():
    for case in test_cases:
        assert string_xor(case[0],case[1]) == case[2], "Incorrect result"
test()
``` 
This code defines a function called `string_xor` that performs the XOR operation of two strings. It uses the string representation and the `ord` function to convert the strings to integers, and then uses the `chr` function to convert the integers back to their corresponding characters. The code then defines a test cases and a test function to verify that the `string_xor` function produces the correct results for all of the test cases.