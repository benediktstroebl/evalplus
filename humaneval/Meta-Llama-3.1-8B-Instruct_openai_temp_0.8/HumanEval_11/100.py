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
        str: Result of binary XOR operation on strings a and b.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    
    # Use zip to iterate over characters of a and b in parallel
    # and use a generator expression to perform the XOR operation
    # The built-in int function is used to convert the character to an integer
    # The result is converted back to a character using chr, and the '0' string
    # is used to fix the result to a string
    result = ''.join('0' if (int(c1) + int(c2)) % 2 == 0 else '1' for c1, c2 in zip(a, b))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('1010', '0110'))  # Expected output: '1100'
```

This script defines a function `string_xor` that performs binary XOR on two input strings and returns the result as a string. The function uses the built-in `int` function to convert binary characters to integers, performs the XOR operation, and uses the `chr` function to convert the result back to a character. The `zip` function is used to iterate over the characters of the two input strings in parallel. A generator expression is used to perform the XOR operation on the characters of the two strings.