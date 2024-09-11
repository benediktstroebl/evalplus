### Binary String XOR
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary string result of XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Convert input strings to lists of integers for bitwise operations
    a_list = [int(digit) for digit in a]
    b_list = [int(digit) for digit in b]

    # Use list comprehension to perform XOR operation on each pair of digits
    result_list = [(a + b) % 2 for a, b in zip(a_list, b_list)]

    # Convert the result list back to a string
    result_str = ''.join(map(str, result_list))

    return result_str

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```
This script defines a function `string_xor` that takes two binary strings as input, performs the XOR operation on each pair of digits, and returns the result as a string. The example use case demonstrates how to use the function.