Here is a self-contained Python script with a function that solves the problem of creating a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}"
    # Function Test
    assert string_sequence(0) == '0', "Should return '0' for 0"
    assert string_sequence(1) == '1', "Should return '1' for 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Should return '0 1 2 3 4 5' for 5"
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0', "Should return '0 9 8 7 6 5 4 3 2 1 0' for 10"
    assert len(string_sequence(10)) == 45, "Should have length 45 for 10"
```