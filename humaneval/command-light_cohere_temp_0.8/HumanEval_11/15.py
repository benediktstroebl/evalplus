Certainly! Here's a Python script with a self-contained function that solves the problem of XORing two strings consisting of only ones:
```python
import typing
def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two input strings.
    >>> string_xor('010', '110')
    '100'
    """
    return a ^ b
```
This function performs a XOR operation on the two input strings, which are assumed to contain only single characters. 

It uses the typing module for type hinting and better code documentation.