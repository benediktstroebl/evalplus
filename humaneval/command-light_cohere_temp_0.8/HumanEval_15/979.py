```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}{' ' * (n - 1)}"

def test_string_sequence():
    """Test the function by passing some values and asserting the output"""
    assert string_sequence(0) == '0', "Function failed to generate expected output for 0"
    assert string_sequence(1) == '1', "Function failed to generate expected output for 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function failed to generate expected output for 5"
    assert string_sequence(10) == "0 10 9 8 7 6 5 4 3 2 1", "Function failed to generate expected output for 10"

# Call the function with some values and assert the output matches the expected test cases
test_string_sequence()
```