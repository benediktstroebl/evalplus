```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, consisting only of ones and zeros.
    --> 
    return ''.join(sorted((a|b)[::-1]))

def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('000', '111') == '111'
    assert string_xor('111', '000') == '111'
    assert string_xor('111', '1111') == '1111'
    assert string_xor('1010', '110') == '0110'
    assert string_xor('0000', '1010') == '1010'
    assert string_xor('1111', '0011') == '1111'
```

This Python script presents a function named **`string_xor`** that performs the XOR operation on two strings, ensuring they only contain characters 0 and 1. It uses the sorted((a|b)[::-1]) to achieve this, then returns the result as a string.

The script also includes a **`test_string_xor`** function with several test cases. It asserts that the tests the expected results using the **`string_xor`** function. 
This function is a self-contained solution to the problem of XORing two strings in Markdown code blocks.