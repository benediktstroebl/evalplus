```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Resultant binary string after XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs only contain 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must only contain 1s and 0s")

    # Initialize result string
    result = ''

    # Perform XOR operation on each character in the inputs
    for i in range(max(len(a), len(b))):
        # Get the current bits from the inputs, default to '0' if index is out of range
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'

        # Perform XOR operation on the current bits
        result_bit = '1' if bit_a!= bit_b else '0'
        result += result_bit

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines the `string_xor` function, which takes two binary strings as input, performs XOR operation on them, and returns the result as a binary string. The function includes input validation to ensure that the inputs only contain 1s and 0s. The example usage demonstrates how to call the function with different input strings.