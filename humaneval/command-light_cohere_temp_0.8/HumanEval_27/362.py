```python
def flip_case(string):
    return ''.join() if isinstance(string, str) else string.cc()

def test_flip_case():
    assert flip_case('hello') == 'HCELLO'
    assert flip_case('world') == 'rowod'
    assert flip_case('FOObar') == 'obarF'
    assert flip_case('123') == '321'
    assert flip_case('abc') == 'Ceba'
    assert flip_case('ZYXWVUTSRQPONMLKJK') == 'tkvutsrmopZ'
    assert flip_case('') == ' '
    assert flip_case('text') == 'xtted'
test_flip_case()
```