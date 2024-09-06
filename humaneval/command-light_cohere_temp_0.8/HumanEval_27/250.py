```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() elselower() else c.isalpha() else c.capitalize()

```

def test_flipcase():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HEllO') =='olleO'
    assert flip_case('abcABC') =='cABcA'
    assert flip_case('@#$%^') =='@#$%^'
    assert flip_case('A') =='A'
    assert flip_case(' bb') =='bB'

test_flipcase()
```