```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Parameters:
    a (str): First binary string.
    b (str): Second binary string.

    Returns:
    str: Resultant binary string from XOR operation.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs only consist of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must only consist of 1s and 0s")

    # Use a list comprehension to perform XOR operation
    # If a[i] is '1' and b[i] is '0' or vice versa, it results in '1'
    # If a[i] and b[i] are the same, it results in '0'
    result = ['1' if x!= y else '0' for x, y in zip(a, b)]

    # Join the list into a string
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that performs binary XOR operation on two input strings `a` and `b`. The function first checks if the input strings consist only of 1s and 0s, and raises a `ValueError` if not. It then uses a list comprehension to perform the XOR operation, and finally joins the result list into a string. The script also includes a test case to demonstrate the function's usage.