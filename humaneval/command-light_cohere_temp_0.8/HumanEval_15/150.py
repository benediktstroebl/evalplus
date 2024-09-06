```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}"
    # tests
    assert len(string_sequence(0)) == 1
    assert len(string_sequence(5)) == 6
    assert string_sequence(0)[1:9] == '0'
    assert string_sequence(5)[1:6] == '0 1 2 3 4 5'
    assert string_sequence(10)[1:11] == '0 9 10 11 10 12'
    assert string_sequence(15)[1:16] == '0 14 15 16 15'
```