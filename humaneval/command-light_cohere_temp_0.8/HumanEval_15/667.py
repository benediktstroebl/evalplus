```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} {n+3}"

# Test the function with some parameters and assert the output is as expected
assert str(string_sequence(0)) == '0',
assert str(string_sequence(5)) == '0 1 2 3 4 5'
```