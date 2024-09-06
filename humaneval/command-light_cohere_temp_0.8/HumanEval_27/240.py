```python
def flip_case(string: str) -> str:
    return ''.joincase(string.reset_case() 
```
def test_flipcase():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'dwORld'
    assert flip_case('abc123') == 'CBN123'
    assert flip_case('!@') == '!cmOnE'
def test_flipcase_error():
    with pytest.raises(ValueError):
        flip_case('')
``` 
Here, the code defines a function flip_case that converts a given string to lowercase and vice versa. The test_flipcase module contains test functions to check the correctness of the flip_case function.