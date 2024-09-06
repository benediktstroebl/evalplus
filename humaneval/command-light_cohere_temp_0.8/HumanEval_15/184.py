```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}...".

def test_string_sequence():
    assert string_sequence(0) == '0', "Test case 0 failed"
    assert string_sequence(1) == '1', "Test case 1 failed"
    assert string_sequence(5) == '0 1 2 3 4 5', "Test case 5 failed"
    assert string_sequence(6) == '0 1 2 3 4 5', "Test case 6 failed"
    assert string_sequence(10) == '9 9 8 7 6 5 4 3 2 1 0', "Test case 10 failed"
    assert string_sequence(15) == '14 13 12 11 10 9 8 7 5 3 2 1', "Test case 15 failed"
    return "Success!"

print(test_string_sequence())
```