```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings composed of only ones and zeros.
    >>> print(string_xor('010', '110'))
    '100'
    """
    if not a or not b:
        raise ValueError("Input strings must contain only digits.")
    if len(set(a))) != len(set(b)):
        raise ValueError("Input strings must contain distinct digits.")
    out = ''.join(sorted((ord(c) - ord('0') for c in a + b)))
    return chr(out[0] ^ out[1])

# Example usage
a = '010'
b = '110'
print(string_xor(a, b))  # Output: '100'
```

This Python code defines a function called string_xor that performs a bitwise XOR operation on two input strings containing only digits. The function ensures that the strings contain distinct digits and raise appropriate errors if not. It then performs the important, where the first characters of the input strings are sorted and their binary representation is calculated. Finally, the result is returned as a character, with any carry-over bits truncated to get the XOR value as a single character.