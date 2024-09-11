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
        str: The binary XOR result of the input strings.

    Raises:
        ValueError: If the input strings contain characters other than '0' and '1'.
    """

    # Check if the input strings contain only '0' and '1'
    if not set(a + b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of '0' and '1'")

    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the characters and append the result to the list
        result.append(str(int(char_a) ^ int(char_b)))

    # Join the characters in the list to form the final result string
    return ''.join(result)


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```