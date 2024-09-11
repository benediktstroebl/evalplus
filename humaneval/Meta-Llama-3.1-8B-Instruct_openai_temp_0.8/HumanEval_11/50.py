```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if the input strings are valid (only contain 1s and 0s)
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain 1s and 0s")

    # Initialize an empty list to store the result of the XOR operation
    result = []

    # Iterate over the input strings using the zip function to pair corresponding characters
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation on the paired characters and append the result to the list
        result.append(str(int(char_a) ^ int(char_b)))

    # Join the result list into a string and return it
    return ''.join(result)

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a bitwise XOR operation on each pair of corresponding characters, and returns the result as a string. It includes input validation to ensure the input strings only contain 1s and 0s. The example usage demonstrates the function's behavior with the given test case.