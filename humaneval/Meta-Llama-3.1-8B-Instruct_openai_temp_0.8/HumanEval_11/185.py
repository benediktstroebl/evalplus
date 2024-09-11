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
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Ensure inputs are the same length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Initialize result string
    result = ''

    # Iterate over bits in the inputs
    for i in range(max_len):
        # Perform XOR on the current bits
        bit_xor = '1' if a[i]!= b[i] else '0'
        # Append the result bit to the result string
        result += bit_xor

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
print(string_xor('1', '1'))  # Output: '0'
print(string_xor('0', '0'))  # Output: '0'
print(string_xor('1', '0'))  # Output: '1'
print(string_xor('0', '1'))  # Output: '1'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR result as a string. The function first ensures the inputs are the same length by padding them with zeros. Then, it iterates over the bits in the inputs, performing a binary XOR on each pair of bits and appending the result to the result string. Finally, the script includes some test cases to demonstrate the function's correctness.