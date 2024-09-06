```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings consisting only of ones and zeros.
    return ''.join([xbit_or(a, int(b[i])) for i in range(len(a))])
    """
    return ''.join(char for char in a if char == '1' or char == int(b[i]))
def test_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '011'
    assert string_xor('0000', '1111') == '1111'
    assert string_xor('1010', '1111') == '1111'
if __name__ == "__main__":
    test_xor()
```
This Python script defines a function `string_xor` that performs a binary XOR operation on two input strings. The function takes two strings as parameters, `a` and `b`, and returns their XOR as a string. The XOR operation is performed by converting the input characters to either `1` or their corresponding ASCII integer values, and then performing a bitwise XOR operation on the corresponding numbers. The function also includes a test function `test_xor` which contains a series of tests that validate the correctness of the `string_xor` function.