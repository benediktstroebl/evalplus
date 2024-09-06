```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, performs a bitwise exclusive operation on the two inputs and returns the result as a string.
    Args:
        a: string, first string to XOR.
        b: string, second string to XOR.
    Returns: string containing only ones and zeros.
    """

Returns: str, the result of XOR operation on a and b.
    """
    test_case"""
    return a ^ b

# Test case: XOR of "010" and "110"
test_xor("010", "110")
assert string_xor("010", "110") == "100"

# Test case: XOR of "0011" and "001"
test_xor("0011", "001")
assert string_xor("0011", "001") == "1010"

# Test case: XOR of all characters in "abc" with itself
test_xor("abc")
assert string_xor("abc") == "bcc"

```
This Python script defines a function called `string_xor` that performs a bitwise XOR operation on two input strings, consisting only of ones and zeros. The function returns the result, and the code provides several test cases to validate its correctness.