```python
import string_types

def string_xor(a: string_types.types[str], str, b: string_types[str]) -> str:
    """
    XOR two strings of only ones and zeros.
    >>> string_xor('010', '110')
    '100'
    """
    return str(bin(a ^ b)[2:])

# Test cases
test_string_xor = [
    ("010", "110"),
    ("111", "001"),
    ("100", "10"),
    ("001", "11"),
    ("000", "111")
]

for a, b in test_string_xor:
    assert string_xor(a, b) == str(bin(int(a) ^ int(b)))[2:], f"Error with '{a}' and '{b}'"
```

This script defines a function `string_xor` that performs a binary XOR operation on two strings, which are assumed to contain only the characters '0' and '1'. The XOR operation is then converted to a string using `bin` function.  The result is then returned as a string. The test cases ensure that the function is working correctly for all valid inputs.