### Binary String XOR Function
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
    """
    # Check if both inputs consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Convert binary strings to integers, perform XOR, and convert back to binary
    result = bin(int(a, 2) ^ int(b, 2))[2:]

    # Remove leading zeros if any
    return result.zfill(max(len(a), len(b)))


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
print(string_xor('111', '000'))  # Output: '111'
```
This script defines a function called `string_xor` that performs a binary XOR operation on two input strings. The function checks if the inputs are valid binary strings, converts them to integers, performs the XOR operation, and converts the result back to a binary string. The result is then returned. The function also includes a docstring that explains its purpose, parameters, and return value. In addition, the script includes example usage of the function to demonstrate its behavior.