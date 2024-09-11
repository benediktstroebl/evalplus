```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings a and b, 
    each consisting only of 1s and 0s, and return the result as a string.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR result of a and b.

    Raises:
    ValueError: If either a or b contains characters other than '0' or '1'.
    """

    # Check if inputs are valid binary strings
    if not (set(a) <= {'0', '1'} and set(b) <= {'0', '1'}):
        raise ValueError("Both inputs must be binary strings.")

    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must have the same length.")

    # Perform binary XOR
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result


# Example usage:
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```

This script defines the `string_xor` function that takes two binary strings `a` and `b`, performs binary XOR on them, and returns the result as a string. It includes error checking to ensure that both inputs are valid binary strings of the same length. The example usage demonstrates how to use this function with the provided test case.