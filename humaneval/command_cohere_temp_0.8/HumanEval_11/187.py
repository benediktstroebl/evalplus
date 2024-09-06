```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a) // 3)
```

This approach does the following:
1. Converts both input strings `a` and `b` to binary integers `int(a, 2)` and `int(b, 2)`.
2. Performs an XOR operation on these binary integers.
3. Converts the resulting integer back to a binary string, padding it to the same length as the original strings with leading zeros using `.zfill(len(a) // 3)` (since the length of the result string needs to be a multiple of 3, to preserve the format of the input strings).

The tests for this function can be created as follows:
```python
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '110') == '001'
    assert string_xor('010', '001') == '101'
    assert string_xor('100', '001') == '011'
    assert string_xor('010', '101') == '001'
    assert string_xor('001', '101') == '100'

test_string_xor()
```

This test script provides a number of test cases, each of which verifies that the output of `string_xor()` is correct for a particular input. The `test_string_xor()` function executes these test cases by calling `string_xor()` and comparing the result with the expected output using Python's `assert` statement.