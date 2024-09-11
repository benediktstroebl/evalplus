### Binary XOR of Two Binary Strings

The following Python script defines a function `string_xor` that takes two strings of binary digits (1s and 0s), performs a binary XOR operation on them, and returns the result as a string.

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")
    
    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of 1s and 0s")
    
    # Perform binary XOR operation
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))
    
    return result


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```

### Explanation

1.  The function `string_xor` checks if both input strings have the same length and consist only of 1s and 0s. If not, it raises a `ValueError`.
2.  It uses the `zip` function to iterate over the characters of both strings in parallel.
3.  For each pair of characters, it performs a binary XOR operation by checking if the characters are different. If they are different, it appends '1' to the result; otherwise, it appends '0'.
4.  Finally, it returns the result as a string.