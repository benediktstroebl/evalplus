```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings a and b 
    consisting only of 1s and 0s and return result as a string.

    Args:
        a (str): First input string consisting only of 1s and 0s.
        b (str): Second input string consisting only of 1s and 0s.

    Returns:
        str: Result of binary XOR operation on a and b as a string.

    Raises:
        ValueError: If input strings a or b contain characters other than 1s and 0s.
    """

    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Check if input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")

    # Initialize an empty result string
    result = ''

    # Perform binary XOR operation on each character of the input strings
    for char_a, char_b in zip(a, b):
        # Convert characters to integers, perform XOR operation, and convert back to string
        result += str(int(char_a) ^ int(char_b))

    return result


# Example usage
print(string_xor('010', '110'))  # Outputs: 100
```