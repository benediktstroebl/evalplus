```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}" * (n + 1)

def test_string_sequence():
    """Test the function by taking test cases and checking the output against the expected result."""
    assert string_sequence(0) == '0', "First element should be 0"
    assert string_sequence(1) == '1', "Second element should be 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function doesn't generate expected output"

# Run the above test function to test the implementation
```