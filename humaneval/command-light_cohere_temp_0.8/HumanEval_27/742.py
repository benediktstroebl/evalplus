```python
def flip_case(string: str) -> str:
    return string.flip()

def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('world') == 'WoRLD'
    assert flip_case('sure') == 'ureS'
    assert flip_case('fff') == 'FffF'
    assert flip_case('test') == 'EstT'
test_flip_case()
```