```python
def flip_case(string: str) -> str:
    return ''.joinln(c.case(str(string)) for c in 'ACT')

def test_flip_case():
    assert flip_case('Hello') == 'HElLO'
    assert flip_case('hELLO') == 'hello'
    assert flip_case('ABC') == 'CBC'
    assert flip_case('@#$%^&*()') == '@$.lbcc()
```