```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings and return the result.

    Args:
        a (str): A binary string consisting of 1s and 0s.
        b (str): A binary string consisting of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation on the input strings.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        # If the characters are different (1 and 0, or 0 and 1), the result is 1
        # Otherwise, the result is the same as the character
        result += '1' if char_a!= char_b else '0'

    # Return the resulting string
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their result after performing a binary XOR operation. It uses a simple iteration over the characters in the input strings, performing the XOR operation for each pair of corresponding characters and appending the result to a string. The function also includes a docstring that explains its purpose, input, and output, as well as some example use cases.