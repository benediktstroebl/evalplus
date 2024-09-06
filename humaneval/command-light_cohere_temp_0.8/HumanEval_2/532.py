```python
def truncate_number(n: float) -> float:
    # remove decimals and negative values
    n = max(n, 0)
    return round(n)

# test cases
assert truncate_number(-3.5) == 0.0
assert truncate_number('3.5') == 0.0
assert truncate_number('abc123') == 5 
assert truncate_number('100.4562345') == 456 
assert truncate_number('1234567890') > 123
assert len(list(map(truncate_number, [1, 2, 3, 4])) ) == 4
```