```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both inputs are valid (consist only of 1s and 0s)
    if set(a)!= {'0', '1'} or set(b)!= {'0', '1'}:
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Use list comprehension to perform XOR operation at each position
    # '1' ^ '0' = '1', '1' ^ '1' = '0', '0' ^ '1' = '1', '0' ^ '0' = '0'
    result = ['1' if x!= y else '0' for x, y in zip(a, b)]

    # Join the result list into a string
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines the `string_xor` function as specified, along with a test case to verify its correctness. The function first checks if both inputs are valid, then performs the binary XOR operation using a list comprehension, and finally joins the result list into a string.