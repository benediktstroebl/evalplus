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
        str: Result of binary XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings should consist only of 1s and 0s")

    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Perform XOR operation
    result = int_a ^ int_b

    # Convert result back to binary string
    result_str = bin(result)[2:]

    return result_str

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that performs binary XOR operation on two input strings. It first checks if the input strings consist only of 1s and 0s. Then it converts the binary strings to integers, performs XOR operation, and finally converts the result back to a binary string. The result is returned by the function. The script also includes an example usage of the function.