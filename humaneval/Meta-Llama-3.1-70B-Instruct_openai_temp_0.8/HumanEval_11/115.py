```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): A string consisting only of 1s and 0s.
    b (str): A string consisting only of 1s and 0s.

    Returns:
    str: The result of binary XOR operation on a and b.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both strings must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the strings
    for i in range(len(a)):
        # Perform XOR operation on the characters and append the result to the string
        result += str(int(a[i]) ^ int(b[i]))

    return result

# Test the function
print(string_xor('010', '110'))  # Should print '100'
```