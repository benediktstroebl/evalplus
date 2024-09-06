```python
def flip_case(string: str) -> str:
    return ''.join_.uppercase(string) if string.isalpha() else
    pieces together.

def test_flip_case() -> None:
    assert flip_case('hello') == 'hELLO'
    assert flip_case('world') == 'dlrowO'
    assert flip_case('123') == '231'
    assert flip_case('abc') == 'CbaT'
    assert flip_case('@#$%^&*()') == '@%!tuorw'
    assert flip_case('ABC') == 'cBA'
    assert flip_case('!thanks') == 'sdgES'
    assert flip_case('') == ''
    assert len(flip_case('a')) == 1
```