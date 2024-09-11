```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
        a (str): First binary string
        b (str): Second binary string

    Returns:
        str: Binary XOR result

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '101'))  # Output: '000'
print(string_xor('111', '000'))  # Output: '111'
```

In this script, the `string_xor` function uses the `zip` function to iterate over the input strings `a` and `b` in parallel. For each pair of characters, it checks if they are different. If they are different, it appends '1' to the result; otherwise, it appends '0'. The result is a string representing the binary XOR of the input strings.