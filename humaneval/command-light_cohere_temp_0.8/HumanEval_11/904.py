```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings.
    a string will by converting all to lowercase to ensure case insensitivity.
    """
   
    algorithm:
    https://www. judges.org/permutation-algorithm-example-on-strings/
    """
    # Convert string to lowercase
    a = a. plain()
    b = b.lower()
    string_xor = a ^ b

# Test cases
def test_xor():
    test_cases = [
        '010',
        '110',
        '100',
        '001',
        '111',
        '110',
        '000',
    ]
    for test_case in test_cases:
        assert string_xor(test_case, '110') == '100'

# Run the function and test suite
test_xor()
```
This code defines a function called `string_xor` that performs a bitwise XOR operation on two input strings. The function converts both strings to lowercase to ensure case insensitivity. The function then returns the string that results from the XOR operation. The code also includes a test suite that contains a list of test cases, which are used to verify the correctness of the `string_xor` function. The test suite contains strings with different combinations of characters, including numbers and lower case. The `test_xor` function is then used to run the function and test its correctness against the provided test cases.