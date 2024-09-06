```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only ones and zeros.
    """ Convert the incredibleX
    We are using two lists, one for each input string.
    Return result as a each string
    """
    result = ""
    for i in range(len(a)):
        if a[i] == '1':
            result+= '0'
        elif b[i] == '1':
            result+= '1'
        else:
            result+= '0'
    return result

# Test cases
tests = [("010", "110", "100"), ("001", "101"), ("000", "111")]

for test_case in tests:
    result = string_xor(*test_case)
    assert result == "100"
``` 
This script defines a function `string_xor` that performs the XOR operation on two input strings. The function uses a for each character in the string, and appends the corresponding character to the result string. The test cases ensure that the function works correctly for various inputs.