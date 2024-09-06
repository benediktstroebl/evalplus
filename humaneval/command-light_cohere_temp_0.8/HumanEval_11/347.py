Here is a self-contained Python function that solves the problem you described:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings using 1s and 0s only.
    '1010'
   
    """: (a + b) % 2 for all pairs of characters
    """
    return "".join(chr((a[i] ^ b[i]) % 2 + 2) for i in range(len(a)))
```

This function takes two strings a and b, consisting only of 1s and 0s, and performs a binary XOR operation on all pairs of characters. It then converts theator back string of the result, where each character is either a 1 or a 0. The function then returns the result, which is the string resulting from the XOR operation on the two input strings.