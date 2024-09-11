### Binary String XOR
#### Python Script

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings and return the result as a string.

    Args:
        a (str): First binary string consisting of 1s and 0s.
        b (str): Second binary string consisting of 1s and 0s.

    Returns:
        str: Binary string resulting from XOR operation on inputs a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Use list comprehension to perform XOR operation on corresponding bits
    # 1 XOR 0 = 1, 1 XOR 1 = 0, 0 XOR 0 = 0
    return ''.join('1' if (a_bit == '1' and b_bit == '0') or (a_bit == '0' and b_bit == '1') else '0' 
                   for a_bit, b_bit in zip(a, b))

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that performs binary XOR on two input strings and returns the result as a string. It uses a generator expression and the `zip` function to iterate over corresponding bits in the input strings, applying the XOR operation. The script also includes an example usage and input validation to ensure that the inputs consist only of 1s and 0s.