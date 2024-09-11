### Binary String XOR
#### A Python Function to Perform Binary XOR on Two Input Strings
```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))

        # Append the result to the final result string
        result += xor_result

    # Return the final result
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '110'))  # Output: '011'
```
This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on each pair of characters, and returns the result as a string. The example usage demonstrates how to call the function with different inputs.