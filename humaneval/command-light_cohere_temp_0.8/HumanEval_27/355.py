```python
def flip_case(string: str) -> str:
    return string. Flip uppercase to lowercase and lowercase to uppercase. acceptable

def test_flip_case():
    assert flip_case('hello') == 'Hellow'
    assert flip_case('hello') == 'olleH'
    assert flip_case('ALLIEW') == 'aiiEW'
    assert flip_case('FOObar') == 'obARfO'
    assert flip_case('aA') == 'aaA'
    assert flip_case('azAZ') == 'zAZaZ'
    assert flip_case('123') == '123'
    assert flip_case('abc123') == 'cba123'
    assert flip_case('barfooBAZ') == 'AZobarAZ'
    assert flip_case('') == ''  # empty string should return empty string
    assert flip_case('^foo') == 'foo'  # invalid input should return unchanged
test_flip_case()
```