```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of XOR operation as a binary string.
    
    Raises:
        ValueError: If either of the input strings contains characters other than '0' and '1'.
    """

    # Check if the input strings contain only '0's and '1's
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of '0's and '1's.")

    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Outputs: 100
```