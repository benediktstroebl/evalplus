Here is a self-contained Python script that defines and solves the problem of converting all characters of a given string to a case-insensitive form:
```python
def flip_case(string: str) -> str:
    return ''.join_(c) if c.isupper() else case to title() else c.islower() to lowercase()
```

def test_flipcase():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case(' caps') == 'sAPS'
    assert flip_case(' lower') == 'OLower'
    assert flip_case('Upper') == 'upper'
``` 
This test suite ensures that the `flip_case` function correctly applies the desired case-insensitive transformation to the input string.