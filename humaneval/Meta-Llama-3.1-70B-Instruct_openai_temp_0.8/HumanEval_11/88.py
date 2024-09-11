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

    Raises:
        ValueError: If either string contains characters other than '0' and '1'.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Check if strings contain only '0' and '1'
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both strings must consist only of '0' and '1'")

    # Initialize an empty result string
    result = ""

    # Perform binary XOR operation
    for i in range(len(a)):
        # XOR corresponding bits
        bit = '1' if (a[i]!= b[i]) else '0'
        result += bit

    return result


# Example usage:
print(string_xor('010', '110'))  # Outputs: '100'
```

This script defines a function `string_xor` that performs a binary XOR operation on two input strings `a` and `b`, both consisting only of '0' and '1' characters. The function first checks if the input strings have the same length and only contain '0' and '1' characters. It then initializes an empty result string and iterates over the input strings, performing the XOR operation on corresponding bits and appending the results to the result string. The function returns the result string.

You can use this function to perform binary XOR operations on any two strings consisting only of '0' and '1' characters, as demonstrated in the example usage at the end of the script.