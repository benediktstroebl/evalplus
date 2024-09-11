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
    str: Result of binary XOR operation on a and b.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    if set(a)!= {'0', '1'} or set(b)!= {'0', '1'}:
        raise ValueError("Input strings should only contain 0s and 1s")

    # Convert input strings to lists of integers for easy XOR operation
    list_a = [int(i) for i in a]
    list_b = [int(i) for i in b]

    # Perform XOR operation on corresponding elements
    result = [x ^ y for x, y in zip(list_a, list_b)]

    # Convert the result back to a string
    return ''.join(map(str, result))


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This Python script defines a function `string_xor` that performs binary XOR operation on two input strings. It checks if the input strings contain only 0s and 1s, and then uses a list comprehension to perform the XOR operation on corresponding elements of the two input lists. Finally, it converts the result back to a string and returns it. The example usage at the end demonstrates how to use this function.