```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of binary XOR operation on a and b.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# example usage
print(string_xor('010', '110'))  # output: '100'
print(string_xor('111', '000'))  # output: '111'
print(string_xor('101', '101'))  # output: '000'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR result. The function uses a generator expression with `zip` to iterate over corresponding characters in the input strings, applying the XOR condition. The result is then joined into a single string using `''.join()`. 

Note that this function assumes the input strings only contain '0's and '1's. If the input strings may contain other characters, you should add error checking code to handle this case.