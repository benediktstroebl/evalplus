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
        str: Result of XOR operation as a binary string.

    >>> string_xor('010', '110')
    '100'
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Expected output: '100'
    try:
        print(string_xor('010', '1010'))  # Expected error: ValueError
    except ValueError as e:
        print(e)
```

This script defines a function `string_xor` that takes two binary strings as input, performs an XOR operation on them, and returns the result as a binary string. The function checks if the input strings are of the same length and raises a `ValueError` if they are not. It uses a generator expression with `zip` to iterate over the input strings in parallel and applies the XOR logic. In the example usage, we demonstrate the function's behavior with a valid input and an invalid input that raises an error.