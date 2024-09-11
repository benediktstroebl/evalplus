```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two binary strings.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the XOR operation as a binary string.

    Raises:
    ValueError: If either of the input strings contains characters other than '0' and '1'.
    """

    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")

    # Check if both strings contain only '0's and '1's
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of '0's and '1's.")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        # In Python, '0' is considered False and '1' is considered True
        # So, XOR operation can be performed using the!= operator
        xor_result = '1' if char_a!= char_b else '0'
        
        # Append the result to the result string
        result += xor_result

    # Return the result string
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input and returns their XOR result as a binary string. The function checks if both input strings have the same length and contain only '0's and '1's. It then performs the XOR operation on the input strings using the `!=` operator, which returns `True` if the operands are different and `False` otherwise. The result is appended to the `result` string, which is returned at the end. The script also includes a test case to verify the function's correctness.