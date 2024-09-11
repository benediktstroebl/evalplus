```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): A binary string consisting only of 1s and 0s.
    b (str): A binary string consisting only of 1s and 0s.

    Returns:
    str: The binary XOR of the input strings.
    """
    
    # Check if inputs are binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must only consist of 1s and 0s")

    # Use the zip function to iterate over corresponding characters in the input strings
    # The XOR operation is performed using the ^ operator
    # The result is joined back into a string
    return ''.join('1' if a_i!= b_i else '0' for a_i, b_i in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
print(string_xor('101', '111'))  # Expected output: '010'
print(string_xor('000', '000'))  # Expected output: '000'
```

This script defines the `string_xor` function, which takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It also includes a check to ensure that the input strings only consist of 1s and 0s, and provides some test cases to demonstrate the function's behavior.