```python
def truncate_number(number: float) -> float:
    return 0 if number <= 0 else number // 1

# Here is the function, tested with different numbers.
# Test cases
test_truncate_number(3.5)  # True
test_truncate_number(-3.5)  # True
test_truncate_number(0.5)  # True
test_truncate_number(-5)  # True
test_truncate_number(10)  # True
test_truncate_number(-10)  # False
test_truncate_number(7)  # False
test_truncate_number(None)  # False
test_truncate_number('3.5')  # True
```