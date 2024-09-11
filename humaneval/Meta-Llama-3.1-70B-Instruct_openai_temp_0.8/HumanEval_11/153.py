```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function takes two binary strings as input, performs binary XOR operation on them,
    and returns the result as a binary string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR of the input strings.
    """

    # Check if both inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must be of the same length")

    # Check if both inputs consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both input strings must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, checks for errors, and returns their binary XOR. The XOR operation is performed by iterating over the characters in the input strings, converting them to integers, performing the XOR operation, converting the result back to a string, and appending it to the result string.