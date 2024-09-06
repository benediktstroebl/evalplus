```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} {n+3}"

# Test cases
test_sequence = {
    assert string_sequence(0) == '0', "0 should return 0"
    assert string_sequence(1) == '1', "1 should return 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "5 should return 0 1 2 3 4 5"
    assert string_sequence(-1) == '0', "Negative numbers should return 0"
    assert string_sequence(10) == '9 9 8 7 6 5 4 3 2 1', "10 should return 9 9 8 7 6 5 4 3 2 1"
}
```