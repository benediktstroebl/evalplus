### Binary XOR Operation on Binary Strings
#### Python Script

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
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
    
    # Iterate over the input strings character by character
    for i in range(max(len(a), len(b))):
        # Get the current bits from both strings, or the corresponding default value (0)
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'
        
        # Perform the XOR operation on the current bits
        xor_result = '1' if (bit_a == '1' and bit_b == '0') or (bit_a == '0' and bit_b == '1') else '0'
        
        # Append the XOR result to the result string
        result += xor_result
    
    # Return the result string
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR result as a string. It iterates over the input strings character by character, performs the XOR operation on each pair of bits, and appends the result to a string. The function handles input strings of different lengths by using default values (0) for missing bits. The example usage demonstrates the function's behavior with different input pairs.