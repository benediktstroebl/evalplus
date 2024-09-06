```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings, returns result as a string
    """
    return ''.join(c ^ d for c, d in zip(a, b))
#Test cases
assertEqual(string_xor('010', '110'),'100')
assertEqual(string_xor('000', '110'),'100')
assertEqual(string_xor('111', '0111'),'0000')
assertEqual(string_xor('0011', '001010'),'101010)
assertEqual(string_xor('001', '1111'),'1111')
assertNotEqual(string_xor('11', '10'),'01')
# Usage
print(string_xor('COBOL is Great', 'Yes'))
``` 
This version of the function performs the XOR operation on the two input strings, which are only composed of characters 1 and 0. The result is then returned as a string.