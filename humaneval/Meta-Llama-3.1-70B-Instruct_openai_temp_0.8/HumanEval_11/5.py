```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: The result of the binary XOR operation as a string.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the strings
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation and append the result to the string
        result += str(int(char_a) ^ int(char_b))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```