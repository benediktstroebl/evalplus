```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The binary XOR result as a string.
    
    Raises:
        ValueError: If either string contains characters other than '0' or '1'.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")
    
    # Check if both strings consist only of '0's and '1's
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of '0's and '1's.")
    
    # Perform XOR operation on corresponding characters
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result


# Example usage:
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```