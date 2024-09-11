```markdown
### Binary String XOR Operation

This script performs a binary XOR operation on two input strings consisting of 1s and 0s.
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings and return result as a string.

    Args:
        a (str): First input string consisting of 1s and 0s.
        b (str): Second input string consisting of 1s and 0s.

    Returns:
        str: Result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    if set(a).issubset({'0', '1'}) and set(b).issubset({'0', '1'}):
        # Using Python's built-in zip function and dictionary comprehension to XOR corresponding bits
        return ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    else:
        raise ValueError("Input strings must consist only of 1s and 0s")

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '001'))  # Output: '100'
```
This script defines a function `string_xor` that takes two input strings `a` and `b` and returns their binary XOR result as a string. It first checks if the input strings consist only of 1s and 0s. If they do, it uses dictionary comprehension and the `zip` function to XOR corresponding bits and return the result. If the input strings contain invalid characters, it raises a `ValueError`. The script also includes example usage and test cases.