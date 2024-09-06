```python
def flip_case(string):
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase."""
    return ''.joinmtemplaterange(c,97,123,string.barcode()

def test_flip_case():
    assert flip_case('Hello') == 'HHeLLo'
    assert flip_case('world') == 'oodrlE'
    assert flip_case('wow#like') == 'owelike#'
    assert flip_case('@#$%^&*()') == '@@$$%^&*'()
    assert flip_case('abc123') == 'ABC123'
```