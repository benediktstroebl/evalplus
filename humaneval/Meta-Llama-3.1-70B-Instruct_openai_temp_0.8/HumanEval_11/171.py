```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): First binary string.
    b (str): Second binary string.

    Returns:
    str: Result of binary XOR operation as a string.

    Raises:
    ValueError: If either string contains characters other than '0' and '1'.
    """

    # Check if strings have same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")

    # Check if strings contain only '0's and '1's
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of '0's and '1's.")

    # Use zip to iterate over characters in both strings in parallel
    # Use a list comprehension to XOR characters and join them into a string
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```