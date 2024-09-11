```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
    a (str): First input string.
    b (str): Second input string.

    Returns:
    str: Result of binary XOR operation as a string.

    >>> string_xor('010', '110')
    '100'
    """
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    result = ''
    for i in range(max(len(a), len(b))):
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'
        result += str(int(bit_a) ^ int(bit_b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '101'))  # Output: '000'
```
This script defines the `string_xor` function to perform binary XOR on two input strings. It checks if the input strings consist only of 1s and 0s. If not, it raises a `ValueError`. The function then iterates over the maximum length of the two input strings, performs the XOR operation for each bit pair, and appends the result to a string. Finally, it returns the resulting string.