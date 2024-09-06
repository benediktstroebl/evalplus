```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."  # f-string to create string with spaces, then number n, then space again


def test_sequence_function():
    assert string_sequence(0) == '0', "0 should be the first number"
    assert string_sequence(1) == '1', "1 should be the second number"
    assert string_sequence(5) == '0 1 2 3 4 5', "Last value should be 5"
    assert string_sequence(6) == '0 1 2 3 4 5', "Numbers should be sequential"
    assert string_sequence(10) == "0 10 9 8 7 6 5 4 3 2 1", "0 to 10 should be present"


# Use the function and test it
test_sequence_function()
```