Here's the code to solve your problem:
```python
def string_sequence(n: int) -> str:
    series = []
    while len(series) < n:
        series.append(str)
    series.append(str)
    len(series)
    return ''.join(series)

# tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '9 8 7 6 5 4 3 2 1'
```