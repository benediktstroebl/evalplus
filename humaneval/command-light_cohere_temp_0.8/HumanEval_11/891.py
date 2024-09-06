```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two strings
    where only the single characters are kept
    """
    return ''.join(c if c in a else b for c in b)

# Test case:
print(string_xor('010', '110'))  # Expected Output: 100
print(string_xor(''111', '.'))  # Expected Output: '0000'
print(string_xor('', '22'))  # Expected Output: '0000'
print(string_xor('is' , '?is'))  # Expected Output: 'is'
```