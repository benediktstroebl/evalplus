```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR of a and b as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if inputs are strings and only consist of '1' and '0'
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must only contain '1's and '0's")

    # Use list comprehension to perform XOR operation on each character
    result = ''.join('1' if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1') else '0' for i in range(len(a)))

    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```
This script defines a function `string_xor` that performs binary XOR on two input strings and returns the result as a string. It checks if the input strings only consist of '1's and '0's, then uses list comprehension to perform the XOR operation on each character. The result is then returned as a string.