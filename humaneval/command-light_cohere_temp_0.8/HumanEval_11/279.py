```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings using only ones and zeros
    Returns: the string resulting from bitwise XOR of a and b."""
    return f"{'0'[int((a[i] == '1') & 1)]}0{'1'[(int(b[i]) & 1)]}"[i] for i in range(len(a))

# Test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '101'
    assert string_xor('111', '111') == '000'
    assert string_xor('', '') == ''
    assert string_xor('0', '1') == '1'
    assert string_xor('001', '001') == '001'

if __name__ == "__main__":
    test_string_xor()
``` 
This code implements the function `string_xor`, which takes two strings as input and returns the result of the bitwise XOR operation between them. 

The function utilizes the list comprehension and bitwise operations to achieve this. 

Test cases are also provided to ensure the function's correctness.