```python
def flip_case(string):
    return ''.join_lowercase(string.html

def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HELLo') =='oLLo'
    assert flip_case('HELLo World!aASA') =='aAsWOrld'
    assert flip_case('!aASSA') =='assASo'
    assert flip_case('!!!aasp') =='??sp'
```