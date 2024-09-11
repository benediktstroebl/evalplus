```python
from typing import List


def binary_to_int(binary: str) -> int:
    """ Convert binary string to integer """
    return int(binary, 2)


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
    a (str): First binary string.
    b (str): Second binary string.

    Returns:
    str: Binary XOR result of a and b.
    """
    # Convert binary strings to integers
    int_a = binary_to_int(a)
    int_b = binary_to_int(b)
    
    # Perform XOR operation
    xor_result = int_a ^ int_b
    
    # Convert result back to binary string
    xor_result_binary = bin(xor_result)[2:]
    
    # Pad with leading zeros if necessary
    max_len = max(len(a), len(b))
    xor_result_binary = xor_result_binary.zfill(max_len)
    
    return xor_result_binary


# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines a function `string_xor` to perform binary XOR on two input strings, and a helper function `binary_to_int` to convert a binary string to an integer. The function `string_xor` first converts the input strings to integers using `binary_to_int`, performs the XOR operation using the `^` operator, and then converts the result back to a binary string using `bin`. The result is padded with leading zeros if necessary to match the maximum length of the input strings.