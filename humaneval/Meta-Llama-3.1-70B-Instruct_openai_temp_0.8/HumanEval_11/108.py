```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If the input strings are not of the same length or contain characters other than 1s and 0s.
    """
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation on the corresponding characters
        # Convert the characters to integers, perform the XOR, and convert back to a string
        result += str(int(char_a) ^ int(char_b))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```