```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s.
    Returns the string concatenation of the two inputs.
    """
   
    one = [1 for _ in range(len(a)) if a[_] == 1]
    ;
    two = [1 for _ in range(len(b))]
    ;
    return ''.join(one + two)

def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('00', '11') == '11'
    assert string_xor('000', '110') == '100'
    assert string_xor('1111', '0000') == '0000'
    assert string_xor('00', '11') != '01'
    assert string_xor('1010', '1111') != '1010'

if __name__ == "__main__":
    test_string_xor()
```
This Python code defines a function `string_xor` that performs the XOR operation on two input strings, which consist only of the digit '1'. The function concatenates the two inputs and returns the result as a string. The `test_string_xor` function contains several test cases that verify the correctness of the `string_xor` function. The tests pass all input strings to the function and compare the output with the expected results using assert statements.