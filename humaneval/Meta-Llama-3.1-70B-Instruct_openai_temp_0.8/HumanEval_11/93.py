```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If the input strings are not of the same length or contain characters other than 1 and 0.
    """

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings contain characters other than 1 and 0
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation on the current characters
        # The XOR operation returns 1 if the characters are different, 0 if they are the same
        xor_result = '1' if char_a!= char_b else '0'
        
        # Append the result to the result string
        result += xor_result

    # Return the result string
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```