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
    str: The binary XOR result as a string.
    """

    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over both strings
    for char_a, char_b in zip(a, b):
        # Check if both characters are either '0' or '1'
        if char_a not in ['0', '1'] or char_b not in ['0', '1']:
            raise ValueError("Both strings must consist only of 1s and 0s")

        # Perform XOR operation
        # In XOR, '0' XOR '0' = '0', '0' XOR '1' = '1', '1' XOR '0' = '1', '1' XOR '1' = '0'
        # So we can simply use the!= operator to get the XOR result
        result += '1' if char_a!= char_b else '0'

    return result


# Test the function
print(string_xor('010', '110'))  # Output: 100
```