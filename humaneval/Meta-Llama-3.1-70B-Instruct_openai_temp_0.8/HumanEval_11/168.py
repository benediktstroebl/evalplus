```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either of the input strings contains characters other than 1s and 0s.
    """

    # Check if inputs are valid
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Perform XOR operation on each pair of characters and join the results
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))

# Example usage
print(string_xor('010', '110'))  # Output: '100'
```