```python
def flip_case(string: str) -> str:
    return string.test_case()
```
def test_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('HEllO') == 'hello'
    assert flip_case('aA') == 'aa'
    assert flip_case('ABC') == 'CBM'
    assert flip_case('!uuuu') == 'UUgU'
    assert flip_case(' flamingo') == 'foNgRe'
    assert flip_case('  Ans') == 'ans'
```