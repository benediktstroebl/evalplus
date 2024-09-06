```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """Perform XOR operation on two strings, with inputs a and b consisting only of single characters."""
    return "".join(chr(96 ^ c) for c in zip(a, b))
``` 
This function performs an XOR operation on two input strings, which must consist of only single characters. It uses the multith to iterate over the input strings, XORing each character with the corresponding character from the other input, and returning the result as a single character.