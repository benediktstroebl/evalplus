```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}..."

# Test the function with different inputs
def test_sequence(func):
    n = 5
    assert func(n) == '0 5 8 11 14 17'. 

test_sequence(string_sequence)
```