```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings a and b.

    Args:
        a (str): A binary string consisting only of 1s and 0s.
        b (str): A binary string consisting only of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If the input strings are of different lengths or contain characters other than '0' and '1'.
    """
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings only contain '0' and '1'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0' and '1'")

    # Initialize an empty result string
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the characters
        xor_result = str(int(char_a) ^ int(char_b))
        # Append the result to the result string
        result += xor_result

    return result

# Example usage:
print(string_xor('010', '110'))  # Outputs: 100
```