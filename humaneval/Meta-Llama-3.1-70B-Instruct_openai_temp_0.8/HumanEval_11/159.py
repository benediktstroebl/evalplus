```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation as a string.
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must be binary strings")

    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Inputs must have the same length")

    # Use zip to iterate over two strings in parallel
    # Use a list comprehension with XOR operator (^) to calculate result
    # Convert result from integer to binary string using bin() function
    # Remove '0b' prefix from binary string using [2:] slicing
    result = ''.join(bin(int(x) ^ int(y))[2:] for x, y in zip(a, b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: 100
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input, performs binary XOR operation on them, and returns the result as a string. The function checks if the inputs are valid binary strings and have the same length. It uses the `zip` function to iterate over the two strings in parallel, calculates the result using a list comprehension with the XOR operator, and converts the result from integer to binary string using the `bin` function. The example usage demonstrates how to use the function with the provided test case.