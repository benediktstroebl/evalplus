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
        str: The result of XOR operation on a and b as a binary string.

    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1011'))  # Output: '0001'
print(string_xor('1111', '0000'))  # Output: '1111'
```

This Python script defines a function `string_xor` that performs binary XOR operation on two input strings. It checks if the input strings are of equal length, and if not, it raises a `ValueError`. The function uses a generator expression to iterate over the characters of the input strings and applies the XOR operation by comparing each character with its corresponding character in the other string. The result is returned as a string. The script also includes some example use cases to test the function.