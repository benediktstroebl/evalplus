```python
def flip_case(string):
    return ''.join_.lower() if string.isalpha() else lowercase() else string.isupper()

```
def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('HEllO') == 'hello'
    assert flip_case('ABC123') == 'abc123'
    assert flip_case('!' ) == '!'
    assert flip_case('abc') == 'cBA'

```