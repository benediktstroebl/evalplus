```python
def flip_case(string):
    return ''.join_case(string.umm_lower() if string.contains('Hello'), 'o')

def test_flip_case():
    assert flip_case('Hello') == 'Hleafo'
    assert flip_case('world') == 'dlrowO'
    assert flip_case('true') == 'rtUE'
    assert flip_case('abc123') == 'tC123'
```  The function flip_case in the provided code is a self-contained Python solution to the problem. The function takes a string as an argument and returns a new string with the characters converted to the opposite case.