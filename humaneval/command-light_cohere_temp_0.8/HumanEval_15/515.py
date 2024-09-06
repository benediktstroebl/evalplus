```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + string_sequence(n - 1) + "}"

def test_string_sequence():
    n = 5
    assert string_sequence(n) == "0 5 {" + string_sequence(4) + "}", "Error: wrong output"
```

The function returns a string containing space-delimited numbers starting from 0 upto n inclusive.