```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR result of the two input strings.
    """
    
    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use zip to iterate over the two strings in parallel
    # Use a list comprehension to perform the XOR operation for each pair of bits
    # Convert the result back to a string
    result = ''.join('1' if bit1!= bit2 else '0' for bit1, bit2 in zip(a, b))
    
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR result. The function checks if the input strings have the same length and consist only of 1s and 0s. It then uses the `zip` function to iterate over the two strings in parallel, performs the XOR operation for each pair of bits, and converts the result back to a string.

You can use the `string_xor` function by calling it with two binary strings as arguments, as shown in the example usage.