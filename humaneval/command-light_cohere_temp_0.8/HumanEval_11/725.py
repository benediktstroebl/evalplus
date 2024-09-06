```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting only of digits 1 and 0.
    :return "0"*a+"0"*b
    """
    return "0"*a+"0"*b

# Test cases
test_cases = [
    "010", "110", "10110",
    "001", "10",
    "1010", "0110",
    # Add more tests as needed
]

for test_str, expected_result in test_cases:
    print(f"Test case: {{{test_str}}}\t{expected_result}")
    result = string_xor(test_str, test_str)
    print(f"Result: {result}\tShould be {expected_result}")
```
The function performs a binary XOR operation on two strings that only contain digits 1 and 0. The function then returns the string that consists of 0s repeated both in the input strings.