```python
def flip_case(string: str) -> str:
    return ''.join() if not string else string.flip()

def test_flip_case() -> None:
    assert flip_case('hello') == 'olleh'
    assert flip_case('world') == 'rdvlos'
    assert flip_case('satelite') == 'eretail'
    assert flip_case('true') == 'ReiouT'
    assert flip_case('Cohere') == 'herenCo'
    assert flip_case(' How are you?') == '?are uT?'
test_flip_case()
```