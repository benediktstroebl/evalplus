```python
def flip_case(string):
    return ''.join_upper_case(string.


def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('hello world!33834') == 'wORld Ol37'
    assert flip_case('!@') == 'AENo'
    assert flip_case(' Championship') == 'cking_rizance'
    assert flip_case(' ' cue') == '  uEsq '
```