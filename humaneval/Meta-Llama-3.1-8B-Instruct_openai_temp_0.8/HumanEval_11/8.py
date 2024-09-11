### Binary XOR of Binary Strings
#### Problem Description
Given two binary strings `a` and `b`, perform binary XOR operation on them and return the result as a binary string.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR of a and b as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty list to store the XOR result
    result = []

    # Iterate over the characters in the input strings
    for i in range(max(len(a), len(b))):
        # Get the current bits from a and b, or '0' if out of bounds
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'

        # Perform binary XOR and append the result to the list
        result.append(str(int(bit_a) ^ int(bit_b)))

    # Join the result list into a string and return it
    return ''.join(result)

# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1010', '1100'))  # Output: '0110'
```
This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs binary XOR operation on them, and returns the result as a binary string. The function iterates over the characters in the input strings, performs XOR on each pair of bits, and appends the result to a list. Finally, it joins the list into a string and returns it. The example usage demonstrates the function's correctness with various inputs.