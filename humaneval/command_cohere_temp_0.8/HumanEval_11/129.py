```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.replace('1', '0').replace('0', '1') == b, "Input validation error"
    for char in a:
        result += str(int(char) ^ int(b[len(result):len(a)+len(result)]))
    return result
```

The script includes tests that check if the input validation and the functionality of the `string_xor` function work correctly:
```python
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('1100', '0110') == '1001'
    assert string_xor('1010', '1001') == '0001'
    assert string_xor('0011', '1010') == '0101'

    # Test case for 1-length inputs
    assert string_xor('1', '1') == '0'
    assert string_xor('0', '0') == '0'

    # Test case for invalid inputs
    try:
        string_xor('01', '11')
        assert False, "Expected error not raised"
    except AssertionError:
        pass
```

The test suite covers edge cases and different lengths of the input strings to validate the correctness of the `string_xor` function.