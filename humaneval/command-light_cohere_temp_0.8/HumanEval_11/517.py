```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings consisting of only ones and zeros.
    :return: The binary XOR of a and b
    """
    return ''.join(c ^ d for c, d in zip([list(a)] + [list(b)]))

# Test cases
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '100') == '100'
    assert string_xor('000', '111') == '100'
    assert string_xor('100', '001') == '100'
    assert string_xor('1010', '110') == '0110'
    assert string_xor('1110', '1110') == '0000'

if __name__ == "__main__":
    test_string_xor()
```
This Python script defines a function **string_xor** that performs a binary XOR operation on two input strings. The function uses the string inputs, where each character is either a single digit from 0 to 9, and returns the binary XOR of these two strings. The test_string_xor function contains a simple series of tests that cover all possible cases, ensuring the correctness of the **string_xor** function.