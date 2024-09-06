```python
def flip_case(string: str) -> str:
    return ''.join() if not string else string.flip_case() + ''.join()

def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'dwORLD'
    assert flip_case('123 456 7890 ') == '1236578899'
    assert flip_case('!>mission') == 'sygnosis'
    assert flip_case('A a Item') == 'AIITEIAM'
```