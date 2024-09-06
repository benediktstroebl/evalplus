```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, performs binary operation of '^'
    on each character in the string and returns the result.
    : Returns '0's' and '1' as empty strings
    """
    # empty string
    if len(a) == 0 and len(b) == 0:
        return ""

    # xor both the strings
    result = ""
    for c in a + b:
        result += chr(97 ^ int(c))

    return result

# test cases
test_cases = [
    "010", "110", "001", "1010", "0110"
]

for tc in test_cases:
    actual = string_xor(tc[0], tc[1])
    print(f"Case {tc}: {actual}")
``` 
The above Python script defines a function `string_xor` that XORs two input strings. It uses the XOR is a simple character-wise operation on the input strings. It also handles the various edge cases for empty strings.