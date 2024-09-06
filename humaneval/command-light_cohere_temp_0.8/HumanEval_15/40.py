```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + string_sequence(n-1) + "}"

def test_string_sequence():
    assert string_sequence(0) == '0', "String not starting with 0!"
    assert string_sequence(1) == '1', "String not increasing!"
    assert string_sequence(5) == '0 1 2 3 4 5', "String not finishing at 5!"
    assert string_sequence(-1) == '0', "String not handling negative!"
    assert string_sequence(10) == '9 9 8 7 6 5 4 3 2 1 0' , "String not handling 10!"

# Test suite for function
test_string_sequence()
```