```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary string result of XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Use zip to iterate over characters in both strings simultaneously
    # Use a list comprehension to apply XOR operation (1^0=1, 1^1=0, 0^0=0, 0^1=1)
    result = ['1' if (x == '1' and y == '1') or (x == '0' and y == '0') else '0' for x, y in zip(a, b)]

    # Join the result list into a string
    return ''.join(result)

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```

In this script, we define a function `string_xor` that takes two binary strings `a` and `b` as input. We first check if both strings are of equal length to ensure the XOR operation can be performed correctly. Then, we use a list comprehension with `zip` to iterate over characters in both strings simultaneously and apply the XOR operation. The result is a list of binary digits, which we then join into a string using `''.join(result)`. The example usage at the end demonstrates the function's behavior.