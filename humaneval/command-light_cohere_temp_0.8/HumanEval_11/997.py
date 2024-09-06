```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two given strings consisting of only 1s and 0s.
    Return the string in reverse order.
    """
    string_xor('100', '010')
    # Expected Output: '010'
    """
    # Split the string into individual characters
    a = ''.join(char for char in a)
    b = ''.join(char for char in b)

    # XOR two lists of characters
    result = [1 if char != '0' else 0 for char in a] + [1 if char != '0' else 0 for char in b]

    # Join the characters back into a string
    return ''.join(result)

# Tests cases
print(string_xor('010', '110'))  # Expected Output: '100'
print(string_xor('111', '0'))  # Expected Output: '111'
print(string_xor('000', '111'))  # Expected Output: '1111'
print(string_xor('1010', '1010'))  # Expected Output: '1010'
``` 
This Python script provides a function `string_xor` that performs the XOR operation on two input strings. It takes an approach for strings consisting only of the characters '1' and '0', and returns the XOR result as a string.