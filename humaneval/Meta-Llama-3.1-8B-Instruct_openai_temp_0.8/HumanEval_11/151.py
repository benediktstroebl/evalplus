### Binary String XOR
#### Problem Description

Perform binary XOR operation on two input strings consisting only of 1s and 0s.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First input string consisting of 1s and 0s.
        b (str): Second input string consisting of 1s and 0s.

    Returns:
        str: Result of binary XOR as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both inputs consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Use list comprehension to perform XOR operation
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result
```
This function uses the `zip` function to iterate over the input strings in parallel. It then uses a list comprehension to perform the XOR operation, returning the result as a string. The function also includes input validation to ensure that both inputs consist only of 1s and 0s.