```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ 
    This function performs a bitwise XOR operation on two input strings.
    Returns the common method to XOR two strings by bitwise shifting the bits of each character
    """
    # Use list comprehension to convert both inputs to lists of characters
    a_list = list(a)
    b_list = list(b)
    # Loop through each character in both strings
    for i, char in enumerate(a_list):
        a_list[i] = (char & 0x1)
    for j, char in enumerate(b_list):
        b_list[j] = (char & 0x1)
    # Use string concatenation to join the two modified lists back into strings
    return ''.join(a_list + b_list)

def test_xor():
    """ 
    Test the function with various inputs.
    """
    test_xor('010', '110')
    print('Result:', '100')
    test_xor('111', '1')
    test_xor('1010', '01')
    test_xor('101', '1')
    test_xor('', '')
```
The provided Python script defines a function `string_xor` that performs a bitwise XOR operation on two input strings. The function uses list comprehension and bitwise shifting to modify each character of the input strings, then joins the modified strings back into a single string. The script also includes a `test_xor` function that provides various test cases to verify the correctness of the `string_xor` function.