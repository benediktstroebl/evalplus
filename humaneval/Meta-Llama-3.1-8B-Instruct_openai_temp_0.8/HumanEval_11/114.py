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
        str: Result of binary XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both strings consist of only 1s and 0s
    if set(a)!= {'0', '1'} or set(b)!= {'0', '1'}:
        raise ValueError("Both strings must consist of only 1s and 0s.")

    # Use list comprehension and map function to perform XOR operation
    result = ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: 100
print(string_xor('111', '000'))  # Output: 111
```