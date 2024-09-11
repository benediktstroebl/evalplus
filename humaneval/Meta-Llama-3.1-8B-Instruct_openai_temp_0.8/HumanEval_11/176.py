```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The binary string resulting from the XOR operation.
    
    Examples:
    >>> string_xor('010', '110')
    '100'
    """

    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Inputs must be binary strings")

    # Use zip to pair corresponding bits and map XOR operation
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    # If lengths of a and b are different, append remaining bits
    if len(a) > len(b):
        result += a[len(b):]
    elif len(b) > len(a):
        result += b[len(a):]

    return result


# Example usage
print(string_xor('010', '110'))  # Output: 100
```

This code defines a function `string_xor` that takes two binary strings as input, performs binary XOR operation on them, and returns the result as a string. It includes input validation to ensure that the inputs are valid binary strings. If the inputs have different lengths, the function will append the remaining bits from the longer input. The code includes an example usage at the end.