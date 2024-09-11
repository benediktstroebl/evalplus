```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either string contains characters other than '0' and '1'.

    Examples:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if input strings are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0' and '1'.")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")

    # Perform binary XOR operation using zip and a generator expression
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```