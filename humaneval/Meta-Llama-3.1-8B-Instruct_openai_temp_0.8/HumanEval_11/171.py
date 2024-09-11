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
    str: XOR result of a and b as a binary string.

    >>> string_xor('010', '110')
    '100'
    """
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation and convert to string
        result += str(int(char_a) ^ int(char_b))
    
    return result


# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '110'))  # Output: '011'
```

In this script, we define the `string_xor` function that takes two binary strings as input, performs binary XOR operation character by character, and returns the result as a string. The `zip` function is used to iterate over the characters in the input strings in parallel. The `int(char, 2)` function is used to convert the binary characters to integers, and the `^` operator performs the XOR operation. The result is then converted back to a binary string using the `str` function and appended to the `result` string.