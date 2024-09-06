```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function to perform XOR on two strings
    """
    # Check if both input strings are empty
    if not a and not b:
        return ""

    # Check if any input string contains a special character other than '0' or '1'
    if a. string pattern "'[0|1]'?:.
    return "---

    # Regular XOR
    # Remove all characters from both strings except '0' and '1'
    a = ''.join(char for char in a if char=='0')
    b = ''.join(char for char in b if char=='0')

    # Return XOR of the new strings
    return a ^ b
```