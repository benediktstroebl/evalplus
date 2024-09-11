```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first string of 1s and 0s.
    b (str): The second string of 1s and 0s.

    Returns:
    str: The result of binary XOR operation on input strings as a string.

    Raises:
    ValueError: If input strings contain characters other than 1 and 0.
    """

    # Check if input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must contain only 1s and 0s")

    # Ensure both strings are of equal length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Perform XOR operation using zip and a list comprehension
    xor_result = [str(int(x) ^ int(y)) for x, y in zip(a, b)]

    # Join the list into a string and return
    return ''.join(xor_result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```