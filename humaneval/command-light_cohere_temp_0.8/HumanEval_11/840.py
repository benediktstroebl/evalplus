```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two strings a and b and return the result as a string. """
    a XOR operation is by taking the bitwise opposite of each character in 'a' and appending it to the beginning of 'b' until all characters in 'a' are found.
    """
    XOR each pair of characters are the same, the characters are opposite in the output.
    """
    string = ""
    for char in range(96, 0, -1):
        if char in a:  #Check if character is in string 'a'
            b = chr(96 - char)  # Swap the character to the other string
            string += b + b[::-1]  # Append the swapped character and reverse it
    return string

# Test case
string_xor('010', '110')
# Expected Output: 100
``` 
The above script provides a function `string_xor` that performs the XOR operation on a and b, which are two strings consisting only of 1s and 0s.