```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input, where each character can be either a '0' or a '1'. It performs a binary XOR operation on the two strings and returns the result as a single string. 

The `zip` function is used to iterate over corresponding characters in the input strings, and for each pair of characters, the `^` operator is used to perform the bitwise XOR operation on their ASCII codes, converted to integers using `ord()`. The result is then converted back to a character using `chr()` and joined together with '+' to form the output string. 

Overall, this function efficiently computes the binary XOR of two input strings and provides the result as a string output. 

This code can be tested as follows:
```python
# Test case from the problem statement
assert string_xor('010', '110') == '100'

# Additional test cases
assert string_xor('001000', '111100') == '00010'
assert string_xor('111100', '000100') == '11010'
```