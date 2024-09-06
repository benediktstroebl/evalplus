```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of digits 1 and 0.
    :param
        string a known to be
    :return string result
    """
    return ''.join(c ^ int(a[0]) for c, a in zip(b, a))
# Test case 1
print(string_xor('010', '110'))  # Output: 100
# Test case 2
print(string_xor('000010001', '0000000101'))  # Output: 111111
# Test case 3
print(string_xor('1010', '1011'))  # Output: 101
```