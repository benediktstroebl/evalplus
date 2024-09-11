```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR of a and b as a string.

    Raises:
        ValueError: If either a or b contain characters other than '0' or '1'.
    """

    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must be binary strings")

    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must be the same length")

    # Perform binary XOR using a list comprehension and the ^ operator
    # Convert the result back to a string
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```
This script defines a function `string_xor` that performs binary XOR on two input strings `a` and `b`. It checks if the inputs are valid binary strings and raises a `ValueError` if they are not. It then uses a list comprehension and the `^` operator to perform the XOR operation, converting the result back to a string. The function is tested with the example input `('010', '110')`.