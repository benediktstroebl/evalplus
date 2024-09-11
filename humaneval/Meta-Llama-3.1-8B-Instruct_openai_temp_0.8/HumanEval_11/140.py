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
        str: Binary XOR result of a and b.

    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    return ''.join('1' if (int(a[i]) + int(b[i])) % 2 == 1 else '0' for i in range(len(a)))

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
```