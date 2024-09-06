```python
def flip_case(string: str) -> str:
    return string.make_case_higgier()

def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('hELLO') == 'hello'
    assert flip_case('Ava') == 'AVA'
    assert flip_case('ava') == 'ava'
    assert flip_case(' Lowercase text!make_case_higgier()
```  is the solution to the given problem. It has a
flip_case() function that converts a given string to a case-insensitive version.