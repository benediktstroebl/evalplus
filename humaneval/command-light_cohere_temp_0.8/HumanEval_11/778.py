```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings using Python type hints.
    a function performs only on ASCII characters (1-128).
    Returns result of the XOR operation between the two input strings.
    """
string_xor('010', '110')
    # Output: 100
    """
    xored = a ^ b
    return xored

# Test the function with a string containing only zeros
test_string = ""
test_result = string_xor("010", test_string)
print(test_result)  # Output: 100

# Test the function with strings containing only ASCII characters
test_string1 = "01010101010"
test_string2 = "110"
test_result1 = string_xor(test_string1, test_string2)
print(test_result1)  # Output: 0110100

# Test the function with mixed strings
test_string3 = " foo"01010101010 "
test_result2 = string_xor("010", test_string3)
print(test_result2)  # Output: XOR of strings, should be foo
```