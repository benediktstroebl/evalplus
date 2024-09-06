```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + string_sequence(n - 1) + "}" 

def test_string_sequence():
    """Test the function for different inputs"""
    assert string_sequence(0) == "0",    
    assert string_sequence(1) == "1",
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "0 9 8 7 6 5 4 3 2 1"
    assert string_sequence(12345) == "0 12345 1234 8 7 6 5 3 2 1"
```