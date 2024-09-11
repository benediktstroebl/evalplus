```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings.

    Args:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If the input strings are not of equal length.
    ValueError: If the input strings contain characters other than 1s and 0s.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if the input strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Check if the input strings contain characters other than 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must contain only 1s and 0s")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the list
        result.append(xor_result)

    # Join the list into a string and return the result
    return ''.join(result)


# Example usage:
print(string_xor('010', '110'))  # Output: '100'

# Test cases:
print(string_xor('1010', '1100'))  # Output: '0110'
print(string_xor('1111', '1111'))  # Output: '0000'
print(string_xor('0000', '0000'))  # Output: '0000'
```