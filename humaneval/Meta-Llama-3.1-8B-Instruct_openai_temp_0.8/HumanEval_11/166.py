### Binary String XOR
#### Problem Statement
Perform binary XOR operation on two given binary strings.

#### Solution

```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Inputs are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of binary XOR operation between a and b.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize result string with zeros
    result = ''
    # Iterate through each character in both strings
    for i in range(max(len(a), len(b))):
        # Get the character at current index from both strings, or 0 if out of range
        a_bit = a[-1 - i] if i < len(a) else '0'
        b_bit = b[-1 - i] if i < len(b) else '0'
        # Perform binary XOR operation on the current bits
        result = ('1' if (a_bit == '1' and b_bit == '0') or (a_bit == '0' and b_bit == '1') else '0') + result
    return result
```

You can run this script to test the `string_xor` function with the provided example:

```python
print(string_xor('010', '110'))  # Output: '100'
```