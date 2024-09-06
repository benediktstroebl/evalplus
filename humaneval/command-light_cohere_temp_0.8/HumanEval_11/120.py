```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings and return result as a string
    Args:
        a: string, first string
        b: string, second string
    Returns:
        string containing XOR of a and b
    """
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert len(a) == len(b)
    assert all(c == '0' for c in a) and all(c == '1' for c in b)
    return ''.join(a ^ b)
# Examples
print(string_xor('010', '110')) # Output: 100
```