```python
def flip_case(string: str) -> str:
    return ''.join_case(string.

def test_flip_case():
    assert flip_case('hello') == 'HELlo'
    assert flip_case('world') == 'WoRLd'
    assert flip_case('FOO') == 'foO'
    assert flip_case('abc') == 'cBA'
    assert flip_case('Bcd') == 'CDd'
    assert flip_case('ZYXWVUTSRQPONMLKJIHGFEDCBA') == 'zyXWVUTSRQPONMLKJIHGFEDCB'
```
The code above contains a function `flip_case` that converts a given string to lowercase. The function uses the technique of using the `transform()` function to change characters of the string to the case it is supposed to be. The function has corresponding tests to ensure it works correctly.