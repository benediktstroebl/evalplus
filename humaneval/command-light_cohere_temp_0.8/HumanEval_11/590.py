```python
import stringio
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two input strings consisting only of ones and zeros
    """
    return stringio.write(a ^ b, "\n")

def test_string_xor():
    a = "010"
    b = "110"
    result = string_xor(a, b)
    assert result == "100"

    a = "0000"
    b = "001100"
    result = string_xor(a, b)
    assert result == "11000"

    a = "1010"
    b = "0"
    result = string_xor(a, b)
    assert result == "10110"

    a = "00"
    b = "001100"
    result = string_xor(a, b)
    assert result == "111000"

    a = "110"
    b = "0000"
    result = string_xor(a, b)
    assert result == "1001100"
```