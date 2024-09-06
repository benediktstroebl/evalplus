```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings containing only digits 1 and 0 and return the result as a string. """
    1s XOR operation on 0s and 1s is 010 --> 1010
    """
    return a ^ b

# Test case function to check the correctness of the string_xor function
def test_case(test_str: str) -> None:
    expected = "1010"
    actual = string_xor(test_str, test_str)
    if expected == actual:
        print(f"Test passed successfully with input: {test_str}")
    else:
        print(f"Test failed with input: {test_str}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")

# Driver code to run the test case function
test_str = "0101010"
test_case(test_str)
``` 
This script provides a self-contained function `string_xor` that performs the XOR operation on two input strings containing only digits 1 and 0, and returns the result as a string. 

Additionally, there is a `test_case` function that provides test cases for the `string_xor` function to check its correctness, and a driver code to run the test cases.