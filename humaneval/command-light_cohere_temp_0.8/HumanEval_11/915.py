```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings a and b, and return the result as a string.
    Input strings a
    a and b are assumed to contain only single characters (1s and 0s).
    """
    # Convert the input strings to lists of characters
    alist = list(a)
    blist = list(b)

    # Perform XOR on the characters in the strings
    result = ''.join(''.join(x ^ y for alist for blist) for x, y in zip(alist, blist))

    return result

# Example usage
print(string_xor('010', '110'))  # Output: 100
```