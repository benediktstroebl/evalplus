```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.
    
    Args:
    a (str): The first input string.
    b (str): The second input string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")
    
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Perform binary XOR operation
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))
    
    return result


# Example usage:
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```
This script defines the `string_xor` function that takes two strings `a` and `b` as input, checks their validity, and returns the result of the binary XOR operation on these inputs as a string. It also includes an example usage in the `if __name__ == "__main__":` block.