```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If input strings are not of equal length or contain characters other than 1s and 0s.
    """
    # Check if input strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Check if input strings contain only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        # The XOR operation returns 1 if the characters are different, and 0 if they are the same
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the result string
        result += xor_result

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```