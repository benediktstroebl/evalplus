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
        str: The binary result of XOR operation on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Ensure both strings have the same length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Perform XOR operation on each character
    result = ''.join('1' if (a_char == '1' and b_char == '0') or (a_char == '0' and b_char == '1') 
                      else '0' for a_char, b_char in zip(a, b))

    return result


# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script uses a list comprehension with the `zip()` function to iterate over the characters of both strings in parallel. It then uses conditional expressions to perform the XOR operation on each pair of characters. The `zfill()` method is used to pad shorter strings with leading zeros to ensure they have the same length. The joined result is then returned as a string.