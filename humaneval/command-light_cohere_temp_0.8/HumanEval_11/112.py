```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    """
   
    return ''.join(a^r[::-1] ^ b^r[::-1])
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '01') == '11'
    assert string_xor('030', '1000') =='30'
    assert string_xor('appyAPPY', 'YIPPE') == 'EPIO'
if __name__ == "__main__":
    test_string_xor()
```