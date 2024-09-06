```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings using type hint for better intuition and type checking.
    # Convert input strings into lists of characters
    # XOR is the bitwise operation where the order of inputs doesn't matter
    # i.e., the string_xor('010', '110') is the same as 'string_xor('110', '010')
    #
    # Perform XOR operation on the input lists
    #
    result = []
    for i in range(len(a)):
        result.append(ord(a[i]) ^ ord(b[i]))
    # Convert the character list back into a string
    return ''.join(result)

# Test cases
assert string_xor('010', '110') == '100'
assert string_xor('111', '011') == '100'
assert string_xor('111', '110') == '00'
assert string_xor('00', '11') == '11'
assert string_xor('000111', '11') == '1111'

```
This code defines a function named string_xor that performs the XOR operation on two input strings. It uses a in the list comprehension, converting the input strings into lists of characters. Then, it iterates through the characters in the strings, performing the bitwise XOR operation. Finally, it converts the list of characters back into a string, returning the result. This code is a input strings are '010' and '110', and the output is '100'.

This code provides a self-contained solution that can be easily tested and is particularly useful when you want to ensure your code is correct.