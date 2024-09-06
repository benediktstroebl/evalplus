```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {" + string_sequence(n - 1) + "}" 

def test_string_sequence():
    """Test the function by passing the test cases."""
    assert string_sequence(0) == "0", 
    assert string_sequence(1) == "1",
    assert string_sequence(2) == "02",
    assert string_sequence(3) == "003",
    assert string_sequence(4) == "404",
    assert string_sequence(5) == "012345"
```