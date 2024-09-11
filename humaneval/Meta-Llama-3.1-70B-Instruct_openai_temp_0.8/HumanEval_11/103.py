```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): First input string consisting only of 1s and 0s.
    b (str): Second input string consisting only of 1s and 0s.
    
    Returns:
    str: Result of binary XOR operation as a string.
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    
    result = ''
    for char_a, char_b in zip(a, b):
        if char_a not in ['0', '1'] or char_b not in ['0', '1']:
            raise ValueError("Input strings must consist only of 1s and 0s.")
        
        # Perform XOR operation
        result += '1' if (char_a == '1' and char_b == '0') or (char_a == '0' and char_b == '1') else '0'
    
    return result


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```
This Python script defines the `string_xor` function that takes two input strings `a` and `b`, performs binary XOR operation on them, and returns the result as a string. It also includes a check to ensure the input strings are of the same length and consist only of 1s and 0s.