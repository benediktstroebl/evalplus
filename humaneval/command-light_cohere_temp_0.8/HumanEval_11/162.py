```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings and return the result as a string
    :type a: str, b: str
    :return: str
    """
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert len(a) == len(b)

    # XOR operation
    result = '0' * len(a)

    for i, (a_char, b_char) in enumerate(zip(a, b)):
        result[i] = str(ord(a_char) ^ ord(b_char))

    return result

# Test cases
def test_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '111') == '000'
    assert string_xor('050', '10') == '050'
    assert string_xor('00', '11') == '11'
    assert string_xor('000', '1111') == '1111'

if __name__ == "__main__":
    test_xor()
```

The code you provided is a Python script with a self-contained function `string_xor` that performs a string XOR operation on two input strings. The test_xor function validates the result by asserting that the output of the `string_xor` function for various input combinations matches the expected output.