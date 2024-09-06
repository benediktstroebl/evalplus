```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting of only digits 1 and 0.
    Return the string
    result,
    """
    return a ^ b

# Example usage
a = '010'
b = '110'
result = string_xor(a, b)
print(result)  # Output should be '100'

# Tests
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '101') == '110'
    assert string_xor('000', '111') == '111'
    assert string_xor('1001', '1010') == '0110'
    assert string_xor('1010', '1010') == '1010'
test_string_xor()  # Test framework would run this automatically
```