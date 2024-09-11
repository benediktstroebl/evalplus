```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    Both a and b should consist only of 1s and 0s.
    The result is also returned as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of XOR operation as a binary string.

    Raises:
        ValueError: If either a or b contains characters other than 1s and 0s.
    """

    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must be binary strings (only 1s and 0s)")

    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must have the same length")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        # The XOR operation in binary is equivalent to!= in Python
        xor_result = '1' if char_a!= char_b else '0'
        
        # Append the result to the final string
        result += xor_result

    # Return the final result
    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```