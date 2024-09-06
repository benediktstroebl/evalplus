```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings a and b consisting only of 1s and 0s.
    - Return the string XOR operation on all characters
    - a = '0101010'
    - b = '11010101'
    - return '100'
    """
    return a ^ b

# Test cases
tests = [
    "Input are two strings a and b consisting only of 1s and 0s"
    "String XOR operation on '0101010' and '11010101'"
    "Should return '100'"
    # Add more test cases here
]

# Run function with all tests
print("Result:", string_xor(*tests))
```