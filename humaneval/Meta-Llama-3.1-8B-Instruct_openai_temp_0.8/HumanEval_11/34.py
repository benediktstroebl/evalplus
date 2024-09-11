### Binary String XOR
#### Problem Description
Perform binary XOR operation on two input strings containing only 0s and 1s.

#### Solution
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
        str: Binary string result of XOR operation.
    """
    # Initialize result string
    result = ''

    # Iterate over characters in the input strings
    for i in range(max(len(a), len(b))):
        # Get current characters from both strings (or default to '0' if out of bounds)
        char_a = a[i] if i < len(a) else '0'
        char_b = b[i] if i < len(b) else '0'

        # Perform XOR operation on current characters and append to result
        result += str(int(char_a) ^ int(char_b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```
This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on each corresponding character, and returns the result as a string. The `max` function is used to ensure we process all characters up to the maximum length of the input strings. If a character is out of bounds in one of the strings, it defaults to '0'. The XOR operation is implemented using the bitwise XOR operator (`^`) in combination with the `int` function to convert the characters to integers.