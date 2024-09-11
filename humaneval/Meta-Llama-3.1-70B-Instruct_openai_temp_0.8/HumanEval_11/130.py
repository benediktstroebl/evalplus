```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR result of a and b as a string.

    Raises:
    ValueError: If either a or b contains characters other than 1s and 0s.
    """

    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must be binary strings (only 1s and 0s).")

    # Ensure inputs are of the same length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Perform XOR operation
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines the `string_xor` function that takes two binary strings as input and returns their binary XOR result as a string. It includes input validation to ensure the inputs are valid binary strings. If the inputs are of different lengths, it pads the shorter string with leading zeros to match the length of the longer string. The XOR operation is performed using a generator expression that iterates over the characters of the input strings, converts them to integers, performs the XOR operation, and converts the result back to a string.