```python
def flip_case(string: str) -> str:
    return ''.joincase(string)[::-1] if string else string

# Unit tests
def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HELLO') == 'hello'
    assert flip_case(' Three Pillars )') == 'tHiP ll ''
    assert flip_case('⃣') == ' lowercase '
    assert flip_case('aa') == 'togua'
    assert flip_case('A A') == 'a ta'
```
This script defines a function `flip_case` that converts a given string to lowercase (lowercase characters to uppercase, and vice versa). It also comes with a set of tests (`test_flip_case`) that check the correctness of the function.