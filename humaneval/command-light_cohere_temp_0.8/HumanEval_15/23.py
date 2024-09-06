```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} 0"*n

def test_string_sequence():
    """ Test the function by checking if the returned sequence equals the expected pattern """
    assert str(string_sequence(5)) == "0 5 0 1 2 3 4", "pass"

# Call the function with arguments to test its validity
test_string_sequence()
```