```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 and returning the length of the sequence 
    """ 
    return f"0 {n} " * (n+1)

# Test suite
def test_string_sequence():
    assert len(string_sequence(5)) == 10
    assert string_sequence(0) == '0'
    assert string_sequence(10) == '' # Should return an empty string
    assert string_sequence(4) == '4 3'
    assert string_sequence(15) == '15 14 13 10'
    assert string_sequence(1) == '1'
    assert string_sequence(99999) == '999999' # Should return 999999

# Main function
if __name__ == "__main__":
    test_string_sequence()
```