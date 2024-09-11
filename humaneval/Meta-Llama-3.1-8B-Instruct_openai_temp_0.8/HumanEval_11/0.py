```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input binary strings.
    
    Args:
        a (str): The first binary string consisting of 1s and 0s.
        b (str): The second binary string consisting of 1s and 0s.

    Returns:
        str: The result of XOR operation on the input strings.
    """
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use zip to iterate over the characters in both strings in parallel
    # and use a list comprehension to perform XOR operation
    result = ''.join('1' if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1') else '0' for i in range(max(len(a), len(b))))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '111'))  # Output: '010'
print(string_xor('0', '1'))      # Output: '1'
print(string_xor('1', '0'))      # Output: '1'
```

This script defines a function `string_xor` that performs binary XOR operation on two input binary strings. It checks if the input strings consist only of 1s and 0s, and then uses a list comprehension to perform the XOR operation. Finally, it returns the result as a string.