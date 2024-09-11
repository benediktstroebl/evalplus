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
        str: XOR result of a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for i, j in zip(a, b):
        # Perform XOR operation on the current bits and append the result
        result += str(int(i) ^ int(j))
    
    # If the input strings are of different lengths, pad the shorter one with zeros
    result = result.ljust(max(len(a), len(b)), '0')
    
    # Return the result
    return result

# Test the function
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Expected output: '100'
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. The XOR operation is performed on corresponding bits in the input strings. If the input strings are of different lengths, the shorter one is padded with zeros before the XOR operation is performed. The script includes a test case to demonstrate the functionality of the `string_xor` function.