```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
    a (str): First input string.
    b (str): Second input string.

    Returns:
    str: Result of binary XOR operation as a string.

    Raises:
    ValueError: If input strings do not consist of only 1s and 0s.
    """

    # Check if input strings consist of only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist of only 1s and 0s.")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the characters and append the result to the list
        result.append(str(int(char_a) ^ int(char_b)))

    # Join the characters in the list to form the final result string
    return ''.join(result)

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```