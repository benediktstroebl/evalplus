```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive"""
    return f" {'.join(str(i) for i in range(0, n+1))} "

def test_string_sequence():
    assert string_sequence(0) == '0', "Should start with 0"
    assert string_sequence(1) == '1', "Should start with 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Should end at 5"
    assert string_sequence(10) == '9 9 8 7 6 5 4 3 2 1 0', "Should cover 10"
```