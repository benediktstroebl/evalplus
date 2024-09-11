```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string
        b (str): Second binary string

    Returns:
        str: Binary XOR of a and b as a string

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use built-in zip function to iterate over characters in both strings in parallel
    # Use generator expression to perform XOR operation on each pair of characters
    # Convert the result back to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. The function uses the built-in `zip` function to iterate over the characters in both strings in parallel, a generator expression to perform the XOR operation, and the `join` method to convert the result back to a string. The script then tests the function with several examples.