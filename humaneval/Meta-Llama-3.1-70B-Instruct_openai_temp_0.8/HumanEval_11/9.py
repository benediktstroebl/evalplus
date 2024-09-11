```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings 
    consisting only of 1s and 0s and returns the result as a string.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR result of a and b.

    Raises:
    ValueError: If either a or b contains characters other than '0' and '1'.
    ValueError: If a and b are of different lengths.
    """

    # Check if inputs are strings of the same length consisting only of '0's and '1's
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length.")
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both strings must consist only of '0's and '1's.")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```