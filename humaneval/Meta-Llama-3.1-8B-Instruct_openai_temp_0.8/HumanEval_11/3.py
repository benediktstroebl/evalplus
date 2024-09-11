### Binary XOR String Function
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
        a (str): A string consisting only of 1s and 0s.
        b (str): A string consisting only of 1s and 0s.

    Returns:
        str: The binary XOR result as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty list to store the XOR result
    result = []
    
    # Iterate over the two input strings in parallel
    for bit_a, bit_b in zip(a, b):
        # Perform XOR operation and append the result to the list
        result.append(str(int(bit_a) ^ int(bit_b)))
    
    # Join the list of bits into a single string and return the result
    return ''.join(result)

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```
This script defines a function `string_xor` that takes two binary strings as input, performs an XOR operation on each pair of corresponding bits, and returns the result as a string. The XOR operation is performed using the `^` operator, which is a built-in bitwise XOR operator in Python. The result is then joined into a single string using the `join` method.