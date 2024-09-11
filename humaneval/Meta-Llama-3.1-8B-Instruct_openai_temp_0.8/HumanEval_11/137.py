```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    :param a: First input string (binary)
    :param b: Second input string (binary)
    :return: Binary XOR result as a string
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must only contain '0's and '1's")

    # Use a list comprehension to perform XOR operation for each character
    xor_result = ''.join('1' if (c1!= c2) else '0' for c1, c2 in zip(a, b))
    
    return xor_result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that performs binary XOR operation on two input strings consisting only of '0's and '1's. The function uses a list comprehension to iterate over both input strings in parallel using `zip`, and then joins the result into a single string. It also includes a check to ensure that the input strings contain only '0's and '1's.