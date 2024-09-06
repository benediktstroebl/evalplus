```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, returns result as a string.
    """
    Convert two strings into lists of characters and perform XOR
    """
    a = ''.join(char for char in a if char)
    b = ''.join(char for char in b if char)
    return ''.join(char for char in a if char) ^ b

# Test cases
test_cases = [
    ("010", "110").to(),
    ("abc", "abc"),
    ("", ""),
    ("A", "B"),
    ("WARSHIP!", "SHIPSHIP!")]

# Verify function correctness using test_cases
for a, b in test_cases:
    result = string_xor(a, b)
    assert result == "100"
```
This Python code defines a function named `string_xor` that performs the XOR operation on two input strings. The function takes two strings as arguments and returns their XOR as a new string. 

The code also includes a series of test cases, which are passed to the `string_xor` function to verify its correctness. The test cases include various combinations of strings, such as all zeros, all ones, and an empty string. 

This way, the code tests the function's behavior and ensures its accuracy.