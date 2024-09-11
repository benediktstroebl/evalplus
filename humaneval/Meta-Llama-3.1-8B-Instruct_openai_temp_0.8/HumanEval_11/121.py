```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Resultant binary string after XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation and append the result to the list
        result.append(str(int(char_a) ^ int(char_b)))

    # Join the result list into a string and return it
    return ''.join(result)


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR result. It includes input validation to ensure the input strings consist only of 1s and 0s. The function uses the `zip` function to iterate over the characters in the input strings simultaneously, performs the binary XOR operation on each pair of characters, and appends the result to a list. Finally, the function joins the result list into a string and returns it.