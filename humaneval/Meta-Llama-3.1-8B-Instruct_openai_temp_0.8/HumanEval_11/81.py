```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    The input strings are expected to consist only of 1s and 0s.

    Args:
        a (str): The first string for XOR operation.
        b (str): The second string for XOR operation.

    Returns:
        str: The result of binary XOR operation as a string.
    """
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings should consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ''

    # Perform binary XOR operation on the input strings
    for i in range(max(len(a), len(b))):
        # Get the bits from the end of the strings
        bit_a = a[-1 - i] if i < len(a) else '0'
        bit_b = b[-1 - i] if i < len(b) else '0'

        # Perform XOR operation on the bits
        result = ('1' if (bit_a == '1' and bit_b == '0') or (bit_a == '0' and bit_b == '1') else '0') + result

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This Python script defines a function called `string_xor` that takes two binary strings as input and returns their binary XOR result. It checks if the input strings consist only of 1s and 0s before performing the XOR operation. The result is then returned as a string. The function is tested with an example input to demonstrate its correctness.