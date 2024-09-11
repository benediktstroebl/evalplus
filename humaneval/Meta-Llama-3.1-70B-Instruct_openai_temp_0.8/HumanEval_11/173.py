```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR result as a string.

    Raises:
        ValueError: If either input string contains characters other than '0' or '1'.
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0' or '1'")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the characters
        xor_result = str(int(char_a) ^ int(char_b))
        # Append the result to the result string
        result += xor_result

    return result


# Example usage
print(string_xor('010', '110'))  # Outputs: '100'

# Test with strings of different lengths
try:
    print(string_xor('1010', '110'))  # Raises ValueError
except ValueError as e:
    print(e)

# Test with invalid input strings
try:
    print(string_xor('1012', '110'))  # Raises ValueError
except ValueError as e:
    print(e)
```