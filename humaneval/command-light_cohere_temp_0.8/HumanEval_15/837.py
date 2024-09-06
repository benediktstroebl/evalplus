```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + string_sequence(n - 1) + "}"

def test_string_sequence():
    """Test the function with a parameter value of 5 and expected return value as the string '0 1 2 3 4 5'"""
    assert string_sequence(5) == "0 5 [0 1 2 3 4]"
```