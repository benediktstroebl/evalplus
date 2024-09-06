```python
def flip_case(string: str) -> str:
    """
    Flip all characters in the string, making lowercase characters uppercase and vice versa.
    Returns a string in all case of characters.
    return: 
    """string
    """ 

# Tests 
def test_flip_case():
    assert flip_case('hello') == 'HElLo'
    assert flip_case('HEllO') == 'hello'
    assert flip_case('123') == '231'
    assert flip_case('abc') == 'Cbc'
    assert flip_case('A123') == 'a23' 
    assert flip_case('⚡A23⚡') == 'a23ro' 

# Call the function with tests 
test_flip_case()
```