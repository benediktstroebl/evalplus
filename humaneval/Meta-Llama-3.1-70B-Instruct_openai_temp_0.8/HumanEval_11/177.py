```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either input string contains characters other than 1s and 0s.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must have the same length")

    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both input strings must consist only of 1s and 0s")

    # Perform binary XOR using a list comprehension and the ^ operator
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'

# Test cases:
print(string_xor('000', '000'))  # Output: '000'
print(string_xor('111', '111'))  # Output: '000'
print(string_xor('101', '010'))  # Output: '111'

try:
    print(string_xor('123', '456'))  # Raises ValueError
except ValueError as e:
    print(e)

try:
    print(string_xor('101', '123'))  # Raises ValueError
except ValueError as e:
    print(e)
```