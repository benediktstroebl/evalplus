```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings and return the result as a string.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The binary XOR of the input strings.

    Raises:
    ValueError: If the input strings are not the same length or contain characters other than '0' or '1'.
    """
    # Check if the input strings are the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be the same length")

    # Check if the input strings only contain '0' or '1'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0' or '1'")

    # Perform binary XOR
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result


# Example usage
print(string_xor('010', '110'))  # Output: '100'

# Test the error handling
try:
    print(string_xor('010', '1100'))  # Raises ValueError
except ValueError as e:
    print(e)

try:
    print(string_xor('012', '110'))  # Raises ValueError
except ValueError as e:
    print(e)
```