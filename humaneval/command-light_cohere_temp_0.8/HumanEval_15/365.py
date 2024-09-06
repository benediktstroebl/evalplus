```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."

def test_string_sequence():
    """Test case function"""
    assert str(string_sequence(5)) == "0 5 4 3 2 1"
    assert str(string_sequence(0)) == "0"
    assert str(string_sequence(-1)) == "Invalid input"
```