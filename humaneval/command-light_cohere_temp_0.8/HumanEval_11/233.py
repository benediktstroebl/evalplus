```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    Returns the result of performing XOR operation on two strings.
    a and b consist only of ones and zeros.
    """
    strings are expected to be of length n
    """
    assert len(a)==len(b)
    assert all(c=='0' for c in a) and all(c=='0' for c in b)
    return ''.join(''.join(sorted((a ^ b)))

# Example usage
print(string_xor('010', '110'))  #Expected Output: 100
```