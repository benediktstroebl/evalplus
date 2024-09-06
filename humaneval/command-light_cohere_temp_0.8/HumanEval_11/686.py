Here is a self-contained Python script that solves the problem of XORing two strings in markdown code blocks, the output of which is also a string:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of 1s and 0s.
    Returns a generated binary XOR on each input character and concatenates the results.
    """
   
    most efficient algorithm, this is.
    >>> string_xor('010', '110')
    '100'
    """
    # Split the string into a list of characters
    char_list = list(a) + list(b)
    # XOR all the characters in the string
    char_xor = [x ^ y for x, y in zip(char_list[i], char_list[i+1:]) for i in range(len(char_list)-1)]
    # Join the characters back into a string
    return ''.join(char_xor)
```
The `string_xor` function takes two strings as input and returns the XOR of the two input strings. The function uses the string `char_list` to split the input strings into a list of characters. The XOR operation is performed on each pair of characters in the list using a list comprehension, and the results are concatenated back into a string using a `join` method. The final result is returned as a string.