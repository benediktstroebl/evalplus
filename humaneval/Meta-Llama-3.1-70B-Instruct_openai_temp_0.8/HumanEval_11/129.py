```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first string.
    b (str): The second string.

    Returns:
    str: The result of the binary XOR operation.

    Raises:
    ValueError: If either string contains characters other than 1s and 0s.
    """

    # Check if inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")

    # Check if inputs only contain 1s and 0s
    if not set(a).issubset('10') or not set(b).issubset('10'):
        raise ValueError("Both strings must only contain 1s and 0s.")

    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must be of the same length.")

    # Use zip to iterate over the characters in both strings in parallel
    # Use a list comprehension to perform the XOR operation on each pair of characters
    # '1' XOR '1' equals 0, '1' XOR '0' equals 1, '0' XOR '1' equals 1, '0' XOR '0' equals 0
    # In Python, True is equivalent to 1 and False is equivalent to 0
    # We use the fact that in XOR, 1 XOR 1 = 0, 1 XOR 0 = 1, 0 XOR 1 = 1, 0 XOR 0 = 0
    # We use the fact that in Python, True is equivalent to 1 and False is equivalent to 0
    # We convert the boolean values to integers using the int() function
    # Finally, we convert the integers back to strings using the str() function and join them into a single string
    return ''.join(str(int(x!= y)) for x, y in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Outputs: 100
```