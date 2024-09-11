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
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If the input strings are not the same length or contain characters other than '0' or '1'.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be the same length")

    # Check if both strings only contain '0' and '1'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0' and '1'")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation on the characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result


# Example usage
print(string_xor('010', '110'))  # Outputs: '100'
```