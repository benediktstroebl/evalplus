```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The binary XOR result of the input strings as a string.
    
    Raises:
        ValueError: If the input strings are not of equal length or contain non-binary digits.
    """
    
    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")
    
    # Check if input strings only contain binary digits
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain 1s and 0s")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the input strings in parallel using zip
    for bit_a, bit_b in zip(a, b):
        # Perform binary XOR on the current bits and append the result to the result string
        result += str(int(bit_a) ^ int(bit_b))
    
    return result


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```

This script defines the `string_xor` function as required and includes error checking to ensure that the input strings are of equal length and only contain binary digits. The function uses the `zip` function to iterate over the input strings in parallel, performing binary XOR on corresponding bits using the `^` operator. The result is then returned as a string.

The script also includes example usage and documentation for the `string_xor` function.