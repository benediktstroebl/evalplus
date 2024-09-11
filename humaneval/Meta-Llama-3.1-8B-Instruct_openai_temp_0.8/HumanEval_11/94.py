```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): The first string consisting of 1s and 0s.
    b (str): The second string consisting of 1s and 0s.

    Returns:
    str: The result of the binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty list to store the result of XOR operation
    result = []
    
    # Iterate over the characters in the input strings
    for i, j in zip(a, b):
        # Perform XOR operation and append the result to the list
        # 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, 1 XOR 1 = 0
        result.append('1' if (i == '1' and j == '0') or (i == '0' and j == '1') else '0')
    
    # Join the list into a string and return the result
    return ''.join(result)
```
This script defines a function `string_xor` that takes two strings `a` and `b` as input, performs a binary XOR operation, and returns the result as a string. The function uses a list to store the result of the XOR operation for each pair of characters in the input strings. Finally, it joins the list into a string and returns the result.