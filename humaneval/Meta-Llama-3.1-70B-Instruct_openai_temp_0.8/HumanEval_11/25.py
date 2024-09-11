```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): A string consisting only of 1s and 0s.
        b (str): A string consisting only of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either a or b contains characters other than '0' and '1'.
    """
    # Check if inputs are valid
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both inputs must consist only of 1s and 0s.")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length.")

    # Perform binary XOR
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```

This script defines the `string_xor` function that takes two binary strings `a` and `b` as input, performs a binary XOR operation on them, and returns the result as a string. It also includes error checking to ensure that the inputs are valid binary strings of the same length. The example usage demonstrates how to use the function with the provided test case.