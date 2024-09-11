```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR of a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    result = ''.join('1' if (a_i == '1' and b_i == '0') or (a_i == '0' and b_i == '1') else '0' 
                     for a_i, b_i in zip(a, b))
    
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs binary XOR on them, and returns the result as a string. The XOR operation compares each bit of the first string to the corresponding bit of the second string. If the bits are not the same, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0. The function handles binary strings of any length. The example usage demonstrates how to use this function with different input strings.