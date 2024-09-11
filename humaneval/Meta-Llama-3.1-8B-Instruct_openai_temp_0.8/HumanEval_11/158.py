### Binary String XOR
#### Problem Statement
Perform binary XOR operation on two binary strings.

#### Solution

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for i in range(max(len(a), len(b))):
        # Get the current characters from both strings, defaulting to '0' if out of range
        char_a = a[i] if i < len(a) else '0'
        char_b = b[i] if i < len(b) else '0'
        
        # Perform binary XOR operation and convert the result to a string
        result_bit = str(int(char_a) ^ int(char_b))
        
        # Append the result bit to the result string
        result += result_bit
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1101', '1011'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on each corresponding bit, and returns the result as a string. The function iterates over the characters in the input strings, performs the XOR operation on each bit, and appends the result to a string. The example usage demonstrates the function's behavior with various input combinations.