```python
def truncate_number(number: float) -> float:
    return round(number) // 10

# Test cases
assert truncate_number(3.5) == 0.2
assert truncate_number(2.0) == 0.2
assert truncate_number(5.0) == 0.2
assert truncate_number(-3.5) == -0.2
assert truncate_number(-5.0) == -1.8
assert truncate_number(10.0) == 1.0
assert truncate_number(1.2547) == 1.0
```