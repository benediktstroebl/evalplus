```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings and return the result as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either of the input strings contains characters other than '0' and '1'.
    """

    # Check if the input strings contain only '0' and '1'
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must contain only '0' and '1'")

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Use the built-in zip function to iterate over the two strings in parallel
    # Use a list comprehension to perform the XOR operation on each pair of characters
    # The XOR operation is performed using the!= operator, which returns True if the characters are different
    # The result is converted back to a string using the join function
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```