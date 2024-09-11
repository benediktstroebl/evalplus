### Binary String XOR Function
#### Description
This script defines a function `string_xor` that performs binary XOR operation on two input strings consisting of 1s and 0s.

### Code
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
        a (str): First input string consisting of 1s and 0s.
        b (str): Second input string consisting of 1s and 0s.

    Returns:
        str: The result of binary XOR operation on the input strings.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    result = ''
    for i in range(len(a)):
        if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
            result += '1'
        else:
            result += '0'

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```
This script defines a function `string_xor` that takes two input strings `a` and `b` and performs binary XOR operation on them. The function first checks if the input strings have the same length. If not, it raises a ValueError. Then it iterates over each character in the input strings and performs the XOR operation based on the values of the characters. The result is stored in the `result` string. Finally, the function returns the `result` string.