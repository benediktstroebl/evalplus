```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """Perform XOR operation on two strings a and b and return result as a string."""
    return chr(ord('0') ^ ord(a[0]) ^ ord(b[0])) + str(len(a))

# Test cases
test_string_xor = [
    '010', '110', '100'
]

for test_case in test_string_xor:
    actual = string_xor(test_case[0], test_case[1])
    assert actual == test_case[2], f"Failed test case: {test_case}"
```
This code defines a function called `string_xor` that performs the XOR operation on two input strings and returns the result as a string. It also provides a test cases with a list of strings, and a loop that iterates over these strings. The function then performs the XOR on the first string of each test case, and compares the result with the expected output, asserting if they are equal. 

The `test_string_xor` list contains three strings: '010', '110', and '100'. These strings are passed to the `string_xor` function, and the resulting output is compared to the expected output, '100'.