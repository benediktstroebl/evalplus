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
        str: Result of XOR operation on input strings

    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use map to apply XOR operation on characters in the input strings
    result = ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))
    
    return result

print(string_xor('010', '110'))  # Output: 100
print(string_xor('111', '000'))  # Output: 111
```
This script defines a function `string_xor` that performs binary XOR on two input strings. It checks if the input strings consist only of 1s and 0s. If not, it raises a `ValueError`. Otherwise, it applies the XOR operation on corresponding characters in the input strings using the `map` function and returns the result as a string. The script also includes example use cases.