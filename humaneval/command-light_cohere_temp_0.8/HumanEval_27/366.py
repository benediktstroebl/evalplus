```python
def flip_case(string):
    return ''.join_lowercase(string)

def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HEllO') == 'olleH'
    assert flip_case('isWONDERFUL') == 'WASderUG'
    assert flip_case('FOOL') == 'ool olf'
```
This script defines the `flip_case` function, which takes a string as input and applies a case flipping transformation. The `test_flip_case` function tests this `flip_case` function with various input strings, ensuring the expected output is produced.