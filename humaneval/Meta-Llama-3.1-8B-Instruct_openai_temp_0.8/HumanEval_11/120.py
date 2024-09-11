```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): First input string consisting only of 1s and 0s.
    b (str): Second input string consisting only of 1s and 0s.

    Returns:
    str: Result of binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the input strings
    for i in range(max(len(a), len(b))):
        # Get the current bits from input strings
        bit_a = '0' if i >= len(a) else a[i]
        bit_b = '0' if i >= len(b) else b[i]

        # Perform XOR operation on the current bits
        result_bit = '1' if bit_a!= bit_b else '0'

        # Append the result bit to the result string
        result += result_bit

    return result


# Test the function with example inputs
print(string_xor('010', '110'))  # Output: '100'
```

This Python script defines a function `string_xor` that performs binary XOR on two input strings consisting only of 1s and 0s. It iterates over the input strings, performs XOR operation on the current bits, and appends the result bit to the result string. The function returns the result string after iterating over all input bits.