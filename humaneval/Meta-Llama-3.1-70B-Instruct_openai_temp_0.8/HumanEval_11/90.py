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

    # Check if input strings only contain 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must only contain 1s and 0s")

    # Ensure input strings are of equal length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Perform binary XOR using zip and a list comprehension
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))

    return result

# Example usage
print(string_xor('010', '110'))  # Outputs: '100'
```