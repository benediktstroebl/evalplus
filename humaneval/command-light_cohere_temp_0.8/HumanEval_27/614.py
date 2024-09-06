```python
def flip_case(string: str) -> str:
    return ''.joinb_case(string)

def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('world') == 'oRDl'
    assert flip_case('good night') == 'gnIytN'
``` 
This code has a function that transforms a given string to lowercase, and a test function to check the correctness of the transformation on a few test strings.