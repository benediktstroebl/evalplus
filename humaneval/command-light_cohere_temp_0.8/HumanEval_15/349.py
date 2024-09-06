```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + string_sequence(n - 1) + "}"

def test_string_sequence():
    """Test the function string_sequence with various values of n"""
    assert string_sequence(0) == '0', "0 should be 0"
    assert string_sequence(1) == '1', "1 should be 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "String sequence should be 012345"
    assert string_sequence(10) == "000010", "10 should be 10000"
    assert string_sequence(15) == "012345" , "15 should be 12345"

# Call the test function
test_string_sequence()
```