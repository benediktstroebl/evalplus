```python
def string_sequence(n: int) -> str:
    if n == 0:
        return '0'
    else:
        return str(0) + string_sequence(n-1)

# Test cases
test_string_sequence = [
    assert string_sequence(0) == '0', "Failed: returned '0' for n=0"
    assert string_sequence(1) == '1', "Failed: returned '1' for n=1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Failed: returned incorrect sequence"
    assert string_sequence(-1) == '-1', "Failed: returned incorrect sequence"
    assert string_sequence(10) == '9 9 8 7 6 5 4 3 2 1 0', "Failed: returned incorrect sequence"
]
```