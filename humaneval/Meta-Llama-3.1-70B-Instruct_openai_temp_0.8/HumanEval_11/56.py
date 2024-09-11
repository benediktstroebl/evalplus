```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of only 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either of the input strings contains characters other than '0' and '1'.
    """

    # Check if the input strings are valid
    if not set(a).issubset({'0', '1'}):
        raise ValueError("Input string 'a' must consist only of '0's and '1's.")
    if not set(b).issubset({'0', '1'}):
        raise ValueError("Input string 'b' must consist only of '0's and '1's.")

    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings 'a' and 'b' must have the same length.")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the characters
        xor_result = str(int(char_a) ^ int(char_b))
        # Append the result to the result string
        result += xor_result

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```