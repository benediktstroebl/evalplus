```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two strings consisting only of 1s and 0s
    Args:
        a: string with only 1s and 0s
        b: string with only 1s and 0s
    
    Returns:
        string with only 0s
    """
    # convert string to list of characters
    a = ''.join(a)
    b = ''.join(b)
    
    # XOR operation on list of characters
    return ''.join(a ^ b)

# Test case
print(string_xor('010', '110'))  # prints 100
```