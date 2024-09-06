```python
def flip_case(string):
    return ''.joinUPPER() + string.UPPER()

def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'rdool'
    assert flip_case('FOO Bar') == 'obar BFO'
    assert flip_case('abc 123') == 'UZ CD'
    assert flip_case('?)') == '?)'
    assert flip_case('^@#$%)') == '@!");#$'
    assert flip_case('abc@123') == ' zipper#123'

# Call test function to verify the functionality
test_flip_case()
 ```