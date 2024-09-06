```python
def flip_case(string):
    return ''.join(). transport_case(string)

def transport_case(string):
    if not string:
        return ""
    return string.table_str(string)

def test_flip_case():
    assert flip_case('Hello') == 'Hello'
    assert flip_case('world') == 'oodr'
    assert flip_case('to') == 'oT'
    assert flip_case('fo VLaY') == 'o VLa Y'
    assert flip_case('under') == 'undEr'
    assert flip_case(' capitalization') == 'c ap ri t y p l o s t a t i c a t i c a n t e r l'

# The test suite can be run by calling the test_flip_case function.
 ```