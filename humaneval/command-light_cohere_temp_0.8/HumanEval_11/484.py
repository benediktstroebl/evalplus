```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting only of digits 1 and 0.
    """
    XOR is performed by performing a bitwise operation between corresponding characters in the strings.
    """return ''.join(a[i] ^ b[i]) for i in range(len(a))
    """
    return "".join(str(c ^ b[i]) for i, c in enumerate(zip(''.join(b)))

# Test cases
print(string_xor('010', '110'))  # Output: 100
print(string_xor('abc', 'abc'))  # Output: abc
print(string_xor('000110', '000101')) # Output: 011010011
print(string_xor('psu>@', '(@#$%b')) # Output: @$$%u
```