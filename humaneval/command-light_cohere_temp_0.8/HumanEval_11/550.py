```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings.
    :param a string a str
    : string
    """
    assert len(a) == len(b), "Both inputs must have the same length"
    return "".joinstr(a ^ b)
def test_xor() -> None:
    """
    Test the function by providing input strings with varying lengths and assertions.
    """
    assert string_xor('010', '110') == '100', "Returned string is incorrect"
    assert string_xor('abc', 'abc') == 'abc', "Returned string is incorrect"
    assert string_xor('', '') == '', "Returned string is incorrect"
    assert len(string_xor('abc', 'efg')) == len('abcdefg'), "Returned string is incorrect"
if __name__ == "__main__":
    test_xor()
```