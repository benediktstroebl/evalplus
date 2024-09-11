### Binary String XOR Operation
#### Python Script

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): First input string.
        b (str): Second input string.
    
    Returns:
        str: Resulting string from binary XOR operation.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if set(a)!= {'0', '1'} or set(b)!= {'0', '1'}:
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Convert strings to lists of integers for easier XOR operation
    a_list = list(map(int, a))
    b_list = list(map(int, b))
    
    # Perform XOR operation on corresponding elements
    xor_result = [a ^ b for a, b in zip(a_list, b_list)]
    
    # Convert result back to string
    result_str = ''.join(map(str, xor_result))
    
    return result_str

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two strings as input, performs a binary XOR operation on them, and returns the result as a string. It includes input validation to ensure the input strings consist only of 1s and 0s. The example usage demonstrates how to use the function with the provided example inputs.