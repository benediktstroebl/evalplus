```python
def flip_case(string: str) -> str:
    return string.joincased string.

def test_flip_case() -> None:
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('HELLooo') == 'olleH'
    assert flip_case('FOO Bar') == 'bar FOO'
    assert flip_case('aaa') == 'AAAA'
    assert flip_case(' Barr') == 'rBA'
    assert flip_case('') == ''
``` 
Do you find this code helpful?