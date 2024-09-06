```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, and return result as a string.
    Args:
        a: str, string to perform XOR on.
        b: str, another string to perform XOR on.
    Returns:
    # Perform XOR operation on input strings.
    # Convert thex string
    # to list of integers
    x = [ord(c) for c in a]
    y = [ord(c) for c in b]
    # Perform XOR on lists of integers
    return ''.join([x[i] ^ y[i] for i in range(len(x))])
``` 
The problem is to perform XOR operation on two strings and return the result. 


This function takes two strings a and b as input and performs XOR operation on them. The result is also returned as a string. 

The XOR operation is a logical operation that returns true if the two inputs are different. It returns false if the string and b are equal. 

The Python string is converted into a list of integers using the list comprehension. The list comprehension creates a list where each element is the corresponding character in the input string. The function then performs the XOR operation on each pair of integers in the list, and returns the result. 

The result is then converted back to a string and returned to the calling function.