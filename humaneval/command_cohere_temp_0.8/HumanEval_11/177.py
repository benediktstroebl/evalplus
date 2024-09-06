```python
def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```

This approach does not involve any explicit loops, and it translates the input strings to binary, calculates the binary XOR, and returns the result as a string. Here is a snippet of tests to verify the functionality:
```python
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('1100', '0110') == '1010'
    assert string_xor('0110', '1011') == '0101'
    assert string_xor('1111', '0000') == '0001'
    assert string_xor('0000', '1111') == '1101'
```