```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First input string consisting only of 1s and 0s.
        b (str): Second input string consisting only of 1s and 0s.

    Returns:
        str: Result of binary XOR operation on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    return ''.join('1' if c1!= c2 else '0' for c1, c2 in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```

Note: In the `zip(a, b)` function, both strings `a` and `b` are used to iterate over each character at the same position simultaneously. This is done to compare each character of `a` with the corresponding character of `b` and then apply the XOR operation based on the comparison. The result is then joined into a string using the `join()` function.