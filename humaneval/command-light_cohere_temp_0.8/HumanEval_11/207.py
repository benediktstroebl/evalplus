```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two input strings a and b consisting only of 1s and 0s.
    Return result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Use XOR to perform the operation on characters in strings a and b
    result = ''.join(c ^ int(b[i]) for c, i in zip(a, b))
    return result
``` 
This Python code implements a function named `string_xor` that performs the binary XOR operation on two input strings containing only characters. The code uses the XOR to perform the operation on each pair of corresponding characters from both input strings using a list comprehension. The result is then concatenated with the corresponding reversed string, resulting in the XOR of the two strings.