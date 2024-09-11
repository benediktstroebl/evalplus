```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either input string contains characters other than '0' and '1'.
    """

    # Check if input strings contain only '0's and '1's
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of '0's and '1's")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Use a list comprehension to XOR corresponding characters in the input strings
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```