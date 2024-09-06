```python
def flip_case(string: str) -> str:
    return ''.joinabelize(string.

def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('Some Text 123') == 'sOstriT123'
    assert flip_case('ABC') == 'bcA'
    assert flip_case('abc') == 'CBA'
    assert flip_case(' ‘) == '  '
    assert flip_case(' surprisingly good news! 'FLIPCASE '

test_flip_case()
``` 
This Python code defines a function `flip_case` that transforms a given string by converting lowercase characters to uppercase and vice versa. The code also includes a test function `test_flip_case` with a series of assertions that verify the correctness of the `flip_case` function by passing different input strings.