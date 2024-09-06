```python
def truncate_number(number: float) -> float:
    # Manipulation code goes here 
    return 0.25  # not work as it's already not a decimal number

# Unit Tests
assert truncate_number(3.5) == 0.4
assert truncate_number(4.6) == 0.2
assert truncate_number(0.9) == 0.8
assert truncate_number(-0.9) == 0.8
assert truncate_number(1.4) == 1.2
assert truncate_number(1.8) == 1.6

assert truncate_number(float('123.456')) == 1.456
```