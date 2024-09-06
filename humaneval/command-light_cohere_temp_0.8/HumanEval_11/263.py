Here is a self-contained Python function that solves the problem of XORing two strings consisting only of ones and zeros: 

```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Function to perform XOR on two input strings
    """
    # Remove all non-ASCII characters, convert to lowercase, and remove duplicates
    a = ''.join(c for c in a if c.isalpha and c in b and c in string.isalpha)
   it
   final = a.string()
   string_xor=lambda a, b: a ^ b
```

In this code, we have created a function called `string_xor` that takes two strings as input and returns the XOR of these strings. We then use thel to ensure that the input strings are strings only consisting of characters that are either numbers or letters, removing any non-ASCII characters and converting everything to lowercase.