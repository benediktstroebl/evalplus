```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting only of ones and zeros.
    @ Returns a
            string-like number
    """
    return "".join(*map(str.join, [a ^ b]))
# Test case
def test():
    assert string_xor("010", "110") == "100"
test()
```