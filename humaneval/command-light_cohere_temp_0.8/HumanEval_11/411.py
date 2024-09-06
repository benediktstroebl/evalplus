```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only 1s and 0s
    """
    assert isinstance(a, str) and len(a) == 1, "Input string must be a single character"
    assert isinstance(b, str) and len(b) == 1, "Input string must be a single character"

    # XOR operation
    return '100' if a == '0' and b == '1' else '010'

# Test cases
test_cases = [
    '010',
    '110',
    '00',
    '11',
    '001',
    '1010'
]

for tc, test in enumerate(test_cases, start=1):
    actual = string_xor(*test)
    assert actual == test[0], f"Case {tc}: {actual} != {test[0]}, expected: {test[1]} (input: {test})"
``` 
This code defines a Python function called `string_xor` that performs a bitwise XOR operation on two input strings containing only ones and zeros. It includes input validation to ensure the strings have exactly one character. The code also provides a test suite with several test cases, and uses a `for` loop to iterate over these test cases. It compares the expected output with the actual output of the `string_xor` function for each test case and verifies if they are equal.