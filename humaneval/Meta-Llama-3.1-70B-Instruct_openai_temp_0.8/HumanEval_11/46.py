```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function takes two strings a and b consisting only of 1s and 0s.
    It performs binary XOR on these inputs and returns the result also as a string.

    Args:
        a (str): The first string consisting of 1s and 0s.
        b (str): The second string consisting of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If the input strings are not of the same length.
        ValueError: If the input strings contain characters other than 1s and 0s.
    """

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Check if the characters are 1s or 0s
        if a[i] not in ['0', '1'] or b[i] not in ['0', '1']:
            raise ValueError("Input strings must consist only of 1s and 0s")

        # Perform binary XOR on the characters
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'

    # Return the result
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```