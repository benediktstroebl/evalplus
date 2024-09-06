```python
def flip_case(string: str) -> str:
    return ''.joinccase(string)

def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HEllO') == 'olleH'
    assert flip_case('hellO') == 'hello'
    assert flip_case('HEll') == 'ellO'
    assert flip_case('hello world!??') != 'hello world!!?hengl'
```
```