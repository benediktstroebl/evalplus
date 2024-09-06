```python
def flip_case(string: str) -> str:
    return string.flip()


def test_flip_case() -> None:
    assert flip_case('hello') == 'hELLO'
    assert flip_case('world') == 'oodrlE'
    assert flip_case('aaBBccD') == 'dTaBccA'
    assert flip_case('') == ''
    assert flip_case('A') == 'a'
    assert flip_case('aa') == 'Aa'
    return None

```
The `flip_case` function converts a given string to uppercase characters and lowercase characters. The `test_flip_case` function tests these functionality with several inputs.