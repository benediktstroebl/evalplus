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
        str: Resultant binary string after performing XOR operation.
    
    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are of the same length
    assert len(a) == len(b), "Both strings must have the same length."
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over each character in the input strings
    for i in range(len(a)):
        # Perform XOR operation on the corresponding positions
        # If bits are the same, result is 0; if bits are different, result is 1
        result += str(int(a[i]) ^ int(b[i]))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '111'))  # Output: '000'
print(string_xor('101', '010'))  # Output: '111'
```

This script uses a simple iterative approach to perform the binary XOR operation on the input strings. It checks if the input strings are of the same length, initializes an empty string to store the result, and then iterates over each position in the input strings, performing the XOR operation on the corresponding bits. The result is then returned as a string.