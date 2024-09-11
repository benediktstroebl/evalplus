### Binary String XOR
#### Problem Description
Perform binary XOR operation on two binary strings.

#### Solution

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings in parallel
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current bits and append the result
        result += str(int(char_a) ^ int(char_b))
    
    # If one of the strings is longer than the other, append the remaining bits
    result += a[len(b):] if len(a) > len(b) else b[len(a):]
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR result as a string. The function iterates over the characters in the input strings in parallel, performs XOR operation on the current bits, and appends the result to an empty string. If one of the strings is longer than the other, the remaining bits are appended to the result. The function is then tested with two example inputs.