```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two binary strings.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if the lengths of the input strings are equal
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")

    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Use zip() to iterate over the characters in the input strings in parallel
    # Use a list comprehension to apply the XOR operation to each pair of characters
    # Convert the result to a string using join()
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```