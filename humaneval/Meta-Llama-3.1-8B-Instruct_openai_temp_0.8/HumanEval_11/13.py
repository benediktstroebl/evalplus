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
        str: The result of binary XOR of a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are strings and only contain 1s and 0s
    if not (isinstance(a, str) and isinstance(b, str)):
        raise ValueError("Inputs must be strings")
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must only contain 1s and 0s")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        # Append the result to the list
        result.append(xor_result)

    # Join the result list into a string and return it
    return ''.join(result)


# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines the `string_xor` function, which takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It also includes input validation to ensure that the inputs are strings consisting only of 1s and 0s.