```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR result as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs only consist of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s")

    # Use zip and a list comprehension to perform XOR operation
    # The XOR operation is performed by using a conditional expression:
    #   '1' if the bits are different (a[i]!= b[i]), otherwise '0'
    return ''.join('1' if a_i!= b_i else '0' for a_i, b_i in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '010'))  # Output: '111'
```

Note: This script checks if the input strings consist only of 1s and 0s. If not, it raises a ValueError. The XOR operation is performed using the zip function to pair corresponding bits from the input strings, and then using a list comprehension with a conditional expression to determine the result of each XOR operation.