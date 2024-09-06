```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {" + string_sequence(n - 1) + "}"

def test_string_sequence():
    """ Function to test the string_sequence function """
    assert string_sequence(0) == "0", "0 should be 0"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "0 10 10 10 10"
    assert string_sequence(15) == "0 1 2 3 4 5 6 7 8 9 10"
    assert string_sequence(16) == "0 16 16 16 16"

# Call the function with parameters for test cases
test_string_sequence()
```