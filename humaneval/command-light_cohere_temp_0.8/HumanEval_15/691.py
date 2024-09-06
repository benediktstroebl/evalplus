```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n}"*n

def test_string_sequence(test_n: int) -> None:
    assert test_n == 0
    assert test_n == 1
    assert test_n <= 4
    assert test_string_sequence(test_n) == '0 1 2 3 4'
```