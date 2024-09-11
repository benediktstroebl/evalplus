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
    str: The result of XOR operation as a binary string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Use zip to pair corresponding bits, and use a list comprehension 
    # to apply the XOR operation on each pair
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    # If the input strings are of different lengths, we need to append 
    # zeros to the shorter string to match the length of the longer string
    max_len = max(len(a), len(b))
    result += '0' * (max_len - len(result))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('101', '110'))  # Expected output: '011'
print(string_xor('101', '101'))  # Expected output: '000'
print(string_xor('10', '110'))   # Expected output: '000'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a bit-wise XOR operation on them, and returns the result as a binary string. The function uses the `zip` function to pair corresponding bits from the input strings and a list comprehension to apply the XOR operation. If the input strings are of different lengths, the function appends zeros to the shorter string to match the length of the longer string. The script then tests the function with several examples.