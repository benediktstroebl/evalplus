```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): A binary string.
        b (str): A binary string.

    Returns:
        str: Result of binary XOR between a and b.
    """
    # Check if input strings consist only of 1s and 0s
    if not set(a) <= {'0', '1'} or not set(b) <= {'0', '1'}:
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Initialize an empty string to store result
    result = ""

    # Iterate over characters in input strings
    for i, j in zip(a, b):
        # Perform XOR operation and append result to result string
        result += str(int(i) ^ int(j))

    # If input strings are of different lengths, pad shorter string with zeros
    if len(a) > len(b):
        result += a[len(b):]
    elif len(b) > len(a):
        result += b[len(a):]

    return result


# Test the function
print(string_xor('010', '110'))  # Outputs: '100'
print(string_xor('1010', '1100'))  # Outputs: '0110'
```