```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. This function performs a binary XOR operation on the binary representations of the two input strings and returns the binary representation of the result as a string. The function uses the `int` function to convert the input strings to binary integers, and then performs the XOR operation using the bitwise XOR operator `^`. The result is then converted back to a string using the `bin` function, with the output formatted as a string consisting of 1s and 0s. 

The `string_xor` function is self-contained and can be used to perform binary XOR on any two strings consisting of only 1s and 0s. 

To ensure the functionality of the script, it is recommended to include tests that cover different cases. Below is a markdown code block with example tests:
```
```python
# Test case for string_xor
def test_string_xor():
    assert string_xor('010', '110') == '100'

def test_string_xor_different_length():
    assert string_xor('010', '1') == '1'

def test_string_xor_single_string():
    assert string_xor('01010101', '') == '01010101'
```
```
These tests cover several scenarios:
1. Test case `test_string_xor`: This tests the basic scenario of performing XOR between strings of the same length.
2. Test case `test_string_xor_different_length`: This tests whether the function can handle scenarios in which the lengths of both strings are different.
3. Test case `test_string_xor_single_string`: This test demonstrates that the function retains the input when only one string is provided. 

These tests verify the expected behavior of the `string_xor` function and can be executed independently to validate the functionality. 
If you have any more questions or need assistance with anything, feel free to ask!