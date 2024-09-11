```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If the input strings are not of the same length.
        ValueError: If the input strings contain characters other than 1 and 0.
    """
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings contain only 1s and 0s
    for char in a + b:
        if char not in ['0', '1']:
            raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ""

    # Perform XOR operation on each character of the input strings
    for i in range(len(a)):
        # XOR operation can be performed using the!= operator
        result += '1' if a[i]!= b[i] else '0'

    return result

# Test the function
print(string_xor('010', '110'))  # Expected output: 100
```