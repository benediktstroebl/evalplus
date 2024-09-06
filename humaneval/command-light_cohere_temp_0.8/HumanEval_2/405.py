```python
def truncate_number(number: float) -> float:
    return number - int(number)

# Test cases
assertEqual(truncate_number(3.5), 0.0)
assertTruncate_number(2.0) == 0.0
assertTruncate_number(1.0) == 0.0
assertTruncate_number(0.1) == 0.0
assertTruncate_number(0.5) == 0.0
assertTruncate_number(0.6) == 0.0
assertTruncate_number(1.6) == 0.0
assertTruncate_number(10.0) == 6.0
```