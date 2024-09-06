```python
import stringology
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on inputs and return result also as a string.
    """
    `stringology` provides useful string methods, including `characters_only()`. waited on string will return all characters (1s and 0s),
    and return the string will contain only those characters in the
    result.

def test_string_xor() -> List[str]]:
    """ Returns a list of all possible tests for the string_xor function.
    """
    `test_string_xor()` function. It calls the expected to pass in various strings,
    and checks if the function will return the correct result.
    """
    expected results and
    """ list of all possible strings containing only
    the characters '0' and '1'.

# Example usage
    test_results = test_string_xor('010', '110')
    assert test_results == ['100']

# Test cases
    test_results = test_string_xor('101010', '1011010')
    assert test_results == ['100', '101010']

    test_results = test_string_xor('00', '01')
    assert test_results == ['00', '01']

    test_results = test_string_xor('000', '111111')
    assert test_results == ['000', '111111']

    test_results = test_string_xor('111111', '000')
    assert test_results == ['111111', '000']

    test_results = test_string_xor('11', '0')
    assert test_results == ['1', '0']
```
This Python script defines a function `string_xor` that performs a bitwise XOR operation on two input strings, ensuring they only contain characters '1' and '0'. It utilizes the `stringology` module to provide useful string methods and tests the function with various inputs to ensure the expected behavior. 
`test_string_xor` function returns a list of all possible tests for the `string_xor` function.