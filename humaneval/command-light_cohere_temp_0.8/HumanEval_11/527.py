```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ 
    XOR two strings and return the result as a single string.
    """
    uses type hint: Type[str]
    """
    # Convert the input strings to lists of characters
    alist = [c for c in a]
    blist = [c for c in b]

    # Perform XOR operation on the character lists
    result = [al[i] ^ blist[i] for i in range(len(alist))]

    return ''.join(result)
```