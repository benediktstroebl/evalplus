```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}{' ' * (n - 1)}"
    
def test_string_sequence():
    """Test the function by taking input n and checking the output matches the expected result."""
    assert string_sequence(0) == '0', "First test failed: Function doesn't return '0'"
    assert string_sequence(1) == '1', "Second test failed: Function doesn't return '1'"
    assert string_sequence(5) == '0 1 2 3 4 5', "Third test failed: Function doesn't return expected output"
```