```python
def truncate_number(number: float) -> float:
    return 0.25 if number >= 1 else

    return round(number)

# Test cases
test_truncate_number = [
    float(1),           # Should return 1
    float('inf'),      # Should return 1
    float(-1),       # Should return 1
    float('1.2'),      # Should return 1
    float('1.3'),      # Should return 1
    float('3.0'),     # Should return 1.3

test_truncate_number
```
Do you want help with anything else?