### Binary String XOR Function
#### Problem Description
The function `string_xor` takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a binary string.

#### Code

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings and returns the result as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR result of a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if input strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the list
        result.append(xor_result)

    # Join the result list into a string and return
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```
This script defines the `string_xor` function, which takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a binary string. It also includes a test case to demonstrate the function's usage.