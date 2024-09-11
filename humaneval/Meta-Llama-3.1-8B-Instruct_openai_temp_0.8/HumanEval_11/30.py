```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings and return the result.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR of a and b.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings have the same length by padding with zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Perform XOR operation on corresponding bits and convert to string
    result = ''.join('1' if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1') else '0' for i in range(max_len))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1010', '1100'))  # Output: '0110'
```