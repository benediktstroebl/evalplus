```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}"
    
def test_sequence():
    """Test the function with different inputs"""
    assert string_sequence(0) == '0', "Function doesn't return '0'"
    assert string_sequence(1) == '1', "Function doesn't return '1'"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function doesn't return expected value"
    assert string_sequence(7) == '0 6 7', "Function returns wrong value"
    assert string_sequence(9) == '0 9', "Function returns wrong value"
    assert string_sequence(12) == '0 12', "Function returns wrong value"
    
# Call the test function
test_sequence()
```