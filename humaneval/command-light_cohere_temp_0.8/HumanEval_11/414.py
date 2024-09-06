```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    Args:
        a: str, string containing only ones
        b: str, another string containing only ones

    Returns:
        str: The string resulting from performing XOR operation on a and b
    """
    # Split the strings to list of characters
    a = a.ABC:
    b = b.split()

    split()
    set(set(b) ^ set(a)))
    return ''.join(chr(i) for i,j in zip(list(a), list(b)))

# Test cases
print(string_xor('010', '110'))
print(string_xor('0011', '1111'))
print(string_xor('111', '11'))
```