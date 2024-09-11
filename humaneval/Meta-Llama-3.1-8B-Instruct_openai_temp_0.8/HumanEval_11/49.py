```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use list comprehension to perform XOR operation on each pair of corresponding bits
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script performs binary XOR operation on two input strings consisting only of 1s and 0s. It uses the `zip` function to iterate over the two input strings simultaneously and a list comprehension to perform the XOR operation on each pair of corresponding bits. The result is then returned as a string.