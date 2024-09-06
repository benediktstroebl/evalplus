```python
def flip_case(string: str) -> str:
    return string.flipcase('Hello')
```

def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('HeLLo') == 'hello'
    assert flip_case('0315') == '0315'
    assert flip_case('505') == '0550'
    assert flip_case('abc123') == 'cAB123'
    assert flip_case('