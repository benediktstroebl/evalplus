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

    Raises:
        ValueError: If a or b contain characters other than '0' and '1'.
    """

    # Check if a and b contain only '0's and '1's
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must contain only '0's and '1's")

    # Initialize an empty list to store the XOR result
    xor_result = []

    # Iterate over the characters in a and b
    for char_a, char_b in zip(a, b):
        # Perform XOR on the current characters
        xor_result.append(str(int(char_a) ^ int(char_b)))

    # Join the XOR result into a string
    return ''.join(xor_result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```