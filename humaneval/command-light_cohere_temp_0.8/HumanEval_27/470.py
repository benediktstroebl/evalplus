```python
def flip_case(string):
    return ''.join_case(string.

def _test_flip_case():
    assert flip_case('hello') == 'HEOLLO'
    assert flip_case('world') == 'dlROW'
    assert flip_case('ALL CAPS') == 'llapatSCP'
    assert flip_case('hello world') == 'dlROW OLLA tgll'
    assert flip_case('                    Hello world!') == 'HELLO .nhjwlb'
    assert flip_case('  badAss') == 'sdABAS'

def __starting_point():
    print("Testing function flip_case..." + '\n')
    _test_flip_case()
    print("Starting point completed.  ", end='')
```