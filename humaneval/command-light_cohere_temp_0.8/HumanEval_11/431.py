```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two input strings
    Returns: string XOR of 'a' and 'b'
    """
    return f"{a ^ b}"

# Test cases
tests = [
    "010", "110", "000", "1010", "0110", # Different combinations of 0s and 1s
    "001000", "1000110", # Order matters!

def test_string_xor():
    """ Function to test the string_xor function """
    for test_case, expected_result in tests.
    actual_result = string_xor(*test_case)
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"

# Run the tests
test_string_xor()
``` 
This script defines a `string_xor` function that performs the XOR operation of two input strings, and a `test_string_xor` function to run the function and check the results against the expected output from the `tests` list.