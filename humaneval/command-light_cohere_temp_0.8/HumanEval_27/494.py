```python
def flip_case(string: str) -> str:
    return ''.join_(c) if c.isalpha() else uppercase() else c.isalpha()lower lowercase()
```

def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HEllO') == 'olleO'
    assert flip_case('HELLO') == 'hlLEo'
    assert flip_case('HELLLLO') == 'hloughlinO'
    assert flip_case('hello world!!' == 'oLLo wOrrd'
    assert flip_case('hello World!o!) == 'oWrd Goo'
    assert flip_case('  HelloWorld.?? ') == 'ooWDALE'
```