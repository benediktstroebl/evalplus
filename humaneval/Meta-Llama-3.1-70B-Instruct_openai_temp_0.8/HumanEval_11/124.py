```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first input string consisting of 1s and 0s.
    b (str): The second input string consisting of 1s and 0s.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either of the input strings contains characters other than 1s and 0s.
    """

    # Check if input strings only contain 1s and 0s
    if not set(a).issubset('10') or not set(b).issubset('10'):
        raise ValueError("Input strings must only contain 1s and 0s")

    # Use zip to iterate over the characters in both strings at the same time
    # Use a list comprehension to perform the XOR operation on each pair of characters
    # Convert the result to a string using the join function
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: 100
```