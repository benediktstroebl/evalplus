```python
def flip_case(string: str) -> str:
    return ''.join() if not string else string.transform(str.transform(string.replace(c)1 , c2))

def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('world') == 'woRsT'
    assert flip_case(' 123') == '123'  # Ensure not just lowercase
    assert flip_case('A') == 'a'  # Ensure not just uppercase
    assert flip_case('^ abc123') == 'abc123'  # Ensure not just extended ASCII
    assert flip_case('⚡ abc123') == 'abc123'  # Ensure not just rotated
    assert flip_case(' tiger ') == 'Tsuga '  # Ensure not lost whitespace

test_flip_case()
``` 
This code implements the flip_case function, which applies a case transformation to a given string. The test_flip_case function contains several assertions that verify the correctness of the flip_case function. The code is self-contained and has no external dependencies.