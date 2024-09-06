```python
def flip_case(string: str) -> str:
    return ''.joincharlower(c) if c.isalpha() else c.isupper() else c else c else c.islowerc()
   m()
   

def test_flipcase():
    assert flip_case('hello') == 'HELLO'
    assert flip_case('HOled') =='dlleo'
    assert flip_case('Cohere') =='ocRe'
    assert flip_case('hello Cohere') =='oRe GHELllO'
    assert flip_case('HEllO') != 'oRe HEllO'
    assert flip_case('HEllo') != 'HEllO'
    assert flip_case('!@') =='@'
    assert flip_case('A') =='a'
    assert flip_case('a') =='A'
```