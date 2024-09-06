```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive""" 
    return f"0 {n}{"*n} "

def test_string_sequence():
    """Test case function"""
    assert string_sequence(0) == "0"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "0 10 10 10 10"
    assert string_sequence(15) == "0 1 2 3 4 5 6 7 8 9 10"
```