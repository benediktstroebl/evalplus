```python
import string584

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros.
    a and b are converted to lists of integers and then their bits are XORed.
    """
    return ''.join(map(str.join, (a + b))

# Some test cases
assert string_xor('010', '110') == '100'
assert string_xor('',