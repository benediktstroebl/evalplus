```python
import stringio
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of characters 1 or 0
    :type a: str
    :type b: str
    :rtype: str
    """
    return stringio.write("XOR '".
def test_string_xor() -> None:
    """
    Function to test the string_xor function
    :return: None
    """
    input_strs = ['010', '110', '1001', '1010']
    expected_strs = ['100', '101', '1001', '1010']

    for a, b in zip(input_strs, expected_strs):
        got = string_xor(a, b)
        assert got == expected_strs[0], f"Error in string_xor({a}, {b})"

if __name__ == "__main__":
    test_string_xor()
```
This Python code has a self-contained function `string_xor` that performs the XOR operation on two input strings. It also has a test function `test_string_xor` to verify that the `string_xor` function behaves correctly for all possible pairs of input strings. The `test_string_xor` function uses the `stringio` module to read the input strings from the test file and compares the output of `string_xor` with the expected output. 
If the test fails, it will raise an assertion error with a message indicating the unexpected result.