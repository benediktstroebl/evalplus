```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros.
    Result is a modified binary representation of both input strings.
    """
    strings in reverse order.
    """ Use original input strings reversed.
    """ common prefix is subtract and get the common prefix
    """
    a = a[::-1] + b[::-1]
    return ''.join(a)

# Test cases for the function
test_cases = [
    ("010", "110"),
    ("100", "00"),
    ("001", "11"),
    ("111", "0"),
    ("eps", "")
]

for test_str in test_cases:
    result = string_xor(*test_str)
    assert result == test_str[0] + test_str[1]
``` 
This Python script defines a function `string_xor` that performs the XOR operation on two input strings, consisting only of ones and zeros. It creates the result by first adding the reversed versions of both input strings and then converting it into a string by slicing the resulting string with the alphabet. The test cases are then passed to the function to verify if the result matches the expected output.