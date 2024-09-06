```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else upper() else c.islower() to lower() else c.c else c)string += '')
```

def test_flipcase():
    assert flip_case('Hello') == 'HVELo'
    assert flip_case('hELLO') == 'hello'
    assert flip_case('ALLLLAMA') == 'allLLAMaa'
    assert flip_case(' “ ))}') }') }(‘') == '())) )))'}()'
    assert flip_case('!@.) is not str