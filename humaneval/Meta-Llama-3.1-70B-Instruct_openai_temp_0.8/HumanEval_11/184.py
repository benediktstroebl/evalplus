```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of binary XOR as a string.

    Raises:
    ValueError: If the input strings are not of the same length or contain digits other than 1s and 0s.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise ValueError("Both inputs must be strings.")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must be of the same length.")

    # Check if inputs contain only 1s and 0s
    for char in a + b:
        if char not in ['0', '1']:
            raise ValueError("Input strings can only contain 1s and 0s.")

    # Perform binary XOR using zip and a list comprehension
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result

# Example usage
print(string_xor('010', '110'))  # Outputs: '100'
```