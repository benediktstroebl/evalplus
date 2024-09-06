Here's a self-contained Python script that solves the problem of performing XOR operation on two input strings consisting of only ones:
```python
from typing import List
def string_xor(a: List[str], b: List[str]) -> List[str]:
    """ Performs binary XOR operation on the given strings.
    Returns the the string XOR operation on the given strings.
    Returns a string that is the XOR of a and b
    """
    result = ''.join(c ^ d for c, d in zip(a, b))
    return result
```
This function takes two lists of strings as input and returns the XOR of those strings, which is also a string. It uses the `^zip` method to combine the characters of the two input strings in a consistent way and then returns the result as a string.