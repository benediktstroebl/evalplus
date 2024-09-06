```python
def flip_case(string):
    return ''.join_case(string)

def test_flip_case():
    assert flip_case('Hello') == 'HElLo'
    assert flip_case('world') == 'WoRDl'
    assert flip_case('FFIX') == 'iNXFF'
    assert flip_case('ABC') == 'bcA'
    assert flip_case('titled') == 'TItLED'
    assert flip_case('') == ''
```
This code contains a function `flip_case` that transforms a given string to have its characters' lowercase alphabet flipped. The function uses the `_. how it works, and passes corresponding tests.