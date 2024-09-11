```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR result of a and b as a string.

    Raises:
        ValueError: If the input strings are not of the same length or do not consist of only 1s and 0s.

    Examples:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings consist of only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist of only 1s and 0s")

    # Use zip to pair up corresponding characters in the input strings
    # Use a list comprehension with conditional expressions to perform XOR on each pair
    # Join the XOR results into a single string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```