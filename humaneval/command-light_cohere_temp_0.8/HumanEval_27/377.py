```python
def flip_case(string):
    return ''.join_case(string)

def test_flip_case():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('HeLLo') == 'hello'
    assert flip_case('hello world') == 'WWORLD'
    assert flip_case('hellO door') == 'doO rllo d'
``` 
This script defines a function `flip_case` that converts a given string into a format where the characters' cases are reversed, and a test function `test_flip_case` that checks the function's correctness for a variety of test cases.  The test_flip_case() tests that the function correctly changes the case of characters.