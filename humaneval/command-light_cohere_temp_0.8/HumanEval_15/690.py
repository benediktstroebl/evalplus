```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} " * (n+1) 
def test_sequence(n: int) -> None:
    assert(str(test_sequence(n)) == f"0 {n} 1 2 3 4 5"))
test_sequence(5)
```