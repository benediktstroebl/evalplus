```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either input string contains characters other than '0' and '1'.
    """
    # Check if input strings are valid
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0' and '1'.")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")

    # Initialize an empty result string
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```