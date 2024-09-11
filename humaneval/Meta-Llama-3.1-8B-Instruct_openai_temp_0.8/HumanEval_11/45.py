```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.

    Args:
    a (str): The first binary string consisting only of 1s and 0s.
    b (str): The second binary string consisting only of 1s and 0s.

    Returns:
    str: The result of binary XOR operation as a string.
    """
    # Check if both inputs consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Use list comprehension to perform XOR operation
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` which takes two binary strings `a` and `b` as input, performs binary XOR operation on them, and returns the result as a string. The function first checks if both inputs consist only of 1s and 0s, and raises a `ValueError` if not. It then uses list comprehension and the `zip` function to iterate over the corresponding bits of `a` and `b`, and constructs the result string by concatenating the XOR of these bits.