```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive."""
    return f"0 {n}..."

def test_string_sequence():
    """Test case function to check the correctness of string_sequence function."""
    assert string_sequence(0) == '0', "String sequence starting from 0 is not correct."
    assert string_sequence(1) == '1', "String sequence starting from 1 is not correct."
    assert string_sequence(5) == '0 1 2 3 4 5', "String sequence not correct for n = 5"
```