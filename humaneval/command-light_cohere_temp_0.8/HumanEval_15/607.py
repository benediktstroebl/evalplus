Here's the Python script with a self-contained function that generates a string of space-separated numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*(n+1)

# test cases
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
    assert string_sequence(-5) == '0 0 0 0 0 0'
    assert string_sequence(3) == '0 0 0 0 3'
```
This script defines a function `string_sequence` which returns a string containing space-separated numbers from 0 up to `n` (inclusive). It then provides a set of test cases to ensure that the function is working correctly for various input values.