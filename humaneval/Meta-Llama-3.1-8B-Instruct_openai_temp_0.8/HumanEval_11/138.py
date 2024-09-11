```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR result of a and b.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """

    # Check if both input strings consist only of 1s and 0s
    if set(a).issubset('01') and set(b).issubset('01'):
        
        # Use a list comprehension to perform binary XOR operation
        # The XOR of two bits 'a' and 'b' is 1 if and only if one of them is 1
        result = ''.join('1' if (a_i!= b_i) else '0' for a_i, b_i in zip(a, b))
        
        # If one of the input strings is shorter than the other, 
        # append the remaining bits of the longer string
        result += ''.join(a_i for a_i in a if a_i not in b) 
        result += ''.join(b_i for b_i in b if b_i not in a)
        
        return result
    
    else:
        raise ValueError("Input strings must consist only of 1s and 0s")

# Test the function
print(string_xor('010', '110')) 
print(string_xor('101', '110'))
print(string_xor('101', '101'))
```

In this script, the function `string_xor` takes two binary strings `a` and `b` as input. It first checks if both strings consist only of '1's and '0's. If they do, it uses a list comprehension to perform the binary XOR operation. If one string is shorter than the other, it appends the remaining bits of the longer string. If the input strings do not consist only of '1's and '0's, it raises a ValueError. The script also includes example use cases to demonstrate how to use the function.