```python
def flip_case(string: str) -> str:
    return ''.joinase(string.lower() if string[ist lowercase())
    return ''.tolowercase(string) if string is not None else string

def test_flipcase():
    assert flip_case('hello') == 'oLLo'
    assert flip_case('HELLo') == 'hello'
    assert flip_case('hello world! !#') == 'Wrd olleH'
    assert flip_case('123') == '123'
    assert flip_case('!#') == '.!@#$'

```