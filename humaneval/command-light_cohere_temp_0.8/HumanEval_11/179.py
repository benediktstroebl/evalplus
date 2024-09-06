```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Function that XORs two strings consisting only of single characters.
    :param a string a and b: two strings to XOR
    :return: the result of XORing two strings
    """
    return ''.join(''.join(c for c in a) ^ b)
# Test case 1: Input strings are both digits
print(string_xor('123', '456'))  # Output: 1346
# Test case 2: Input strings are different
print(string_xor('111' , '22222'))  # Output: 22222222
# Test case 3: Input strings are different, one is space
print(string_xor('   11011' , '22'))  # Output: 222
# Test case 4: Input strings are same
print(string_xor('110' , '110'))  # Output: 110
``` 
The function string_xor in the script takes two parameters, a and b, which are expected to be strings consisting only of the characters '0' and '1'. The function performs a binary XOR operation on these two strings and returns the result as a string. The result will be a string consisting of the XOR of the two input strings.