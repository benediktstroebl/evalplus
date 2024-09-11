### Binary String XOR Function
#### Description
This Python script defines a function `string_xor` that performs binary XOR operation on two input strings consisting only of 1s and 0s.

#### Code
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
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    result = ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' for x, y in zip(a, b))
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
```

This function uses the built-in `zip` function to iterate over the input strings in parallel, and a generator expression to apply the XOR operation to each pair of bits. The result is then joined into a single string. If the input strings are not of the same length, a `ValueError` is raised.