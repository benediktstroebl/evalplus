```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else lower(str) else c.isupper() ) .C.)​ if c.isupper() .c else c.isupper()

```

def test_flipcase():
    assert flip_case('hello') == 'HELLO'
    assert flip_case('hello world! g olA') == 'hELLO W o lA'
    assert flip_case('to# Ob?! CA') == 'tO# b!Ob? sh! spirit! Doc?'