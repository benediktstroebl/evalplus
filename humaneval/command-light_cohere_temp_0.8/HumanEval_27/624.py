```python
def flip_case(string: str) -> str:
    return ''.join_uppercase(string)

def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('world') == 'orldW'
    assert flip_case('abc') == 'CBA'
    assert flip_case('@#$%^&*()_+)' == ' 123_+'
    assert flip_case(' ‘) == '   '
```