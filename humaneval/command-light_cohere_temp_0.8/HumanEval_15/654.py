Here is a self-contained Python script that defines a function `string_sequence` solving the given problem:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return "".join(" " * n, ()).
    pass
# tests
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
    assert string_sequence(15) == '0 14 13 12 11 10 9 8 7 6 5 3 2'
```