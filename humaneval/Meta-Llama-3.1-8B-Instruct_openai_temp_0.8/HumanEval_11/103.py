```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Returns:
        str: The result of the binary XOR operation as a string.

    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are of equal length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length.")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the input strings
    for i in range(len(a)):
        # Perform XOR operation on the corresponding bits
        # If they are the same, the result is '0', otherwise it's '1'
        result_bit = '1' if a[i]!= b[i] else '0'
        result += result_bit

    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script uses a simple iteration over the input strings to perform the binary XOR operation. The `result_bit` variable is used to store the result of the XOR operation for each bit, which is then appended to the `result` string. The function also includes a check to ensure that the input strings are of the same length, raising a ValueError if they are not.