```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Use a list comprehension to perform XOR operation on corresponding bits
    result = ['1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b)]
    
    # Join the result list into a string
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script will take two binary strings as input and return their XOR result as a string. The function first checks if the input strings are of the same length. If not, it raises a ValueError. It then uses a list comprehension to perform XOR operation on corresponding bits of the two input strings. The result is a list of strings representing the binary XOR result. Finally, it joins the result list into a string and returns it.