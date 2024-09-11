```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings and return the result as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either string contains characters other than '0' or '1'.
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0's and '1's.")

    # Ensure both strings are the same length by padding the shorter one with zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for i in range(max_len):
        # Perform XOR on the corresponding characters and append the result to the result string
        result += str(int(a[i]) ^ int(b[i]))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```