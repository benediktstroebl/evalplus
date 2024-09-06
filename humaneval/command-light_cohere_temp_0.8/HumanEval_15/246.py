```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n}"
    """return a string containing space-delimited numbers starting from 0 and ending at n inclusive"""
    # tests
    assert string_sequence(0) == '0', "Function failed test with argument 0"
    assert string_sequence(1) == '1', "Function failed test with argument 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function failed test with argument 5"
    assert string_sequence(6) == '0 1 2 3 4', "Function failed test with argument 6"
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0', "Function failed test with argument 10"
    assert string_sequence(5555) == '0 254 253 212 101 99 8', "Function failed test with argument 5555"
```