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
        str: The binary XOR of a and b as a string.

    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    # Use a list comprehension to perform binary XOR on corresponding bits
    result = ['1' if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1') else '0' for i in range(len(a))]
    
    # Join the list into a string
    return ''.join(result)

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR as a string. The function uses a list comprehension to iterate over the bits of the input strings, performing the XOR operation on corresponding bits, and then joins the resulting list into a string. The script also includes a test case to demonstrate the function's usage.