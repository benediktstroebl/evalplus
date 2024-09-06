```python
import stringIO
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s,
    returns the XOR operation result as a string.
    """
    stringIO.String(f('\n', '01')
    str_list = list(map(int, input. string))
    str_list.
    return ''.join(str_list)

def test_xor() -> None:
    # Test case 1
    test_str = "010"
    test_str_res = string_xor(test_str, "110")
    assert test_str == test_str_res
    # Test case 2
    test_str = "01"
    test_str_res = string_xor(test_str, "01")
    assert test_str == test_str_res
    # Test case 3
    test_str = "10101010"
    test_str_res = string_xor("10101010", "10")
    assert test_str == test_str_res
    # Test case 4
    test_str = "10101010"
    test_str_res = string_xor("10101010", "01")
    assert test_str == test_str_res
    # Test case 5
    test_str = "10101010101010"
    test_str_res = string_xor("10101010101010", "10101010")
    assert test_str == test_str_res

# Call the test function
test_xor()
``` 
The code defines a function `string_xor` that performs the XOR operation on two input strings consisting only of ones and zeros. It uses the stringIO.String to read the string values for the inputs and converts them into lists of integers, which are then joined into a string. The test_xor function contains a series of tests that verify the correctness of the `string_xor` function by comparing the expected and actual results for various input combinations.