```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3} " \
        f"{n+4}{n+5}"

# Test the function with some inputs
    assert string_sequence(0) == '0', "Error: 0 should give 0"
    assert string_sequence(1) == '1', "Error: 1 should give 1"
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(7) == '0 7 8 9', "Error: 7 should give 0 7 8 9"
    assert string_sequence(10) == '0 9 10 11 12'
```