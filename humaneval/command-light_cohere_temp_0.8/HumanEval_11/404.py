```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    XOR is XOR on these input strings and return result as a new string.
    """
    Using the XOR in Python is a bit tricky, as there is no built-in method that does what is expected.
    >>> return ''.join(a ^ b)
    """

Here, the `string_xor` function uses the built-in `join()` to perform the XOR operation on two strings and returns the result as a new string.