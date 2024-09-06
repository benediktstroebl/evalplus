Here is a Python script that defines a self-contained function that solves the problem of generating a sequence of numbers in a markdown-formatted string:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"{'0'}{n:0>'\d'}"

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '0 1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
```