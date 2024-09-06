```python
def truncate_number(number: float) -> float:
    # Integer part is the largest integer less than the number
    int_part = number // min(number, 1)
    return int_part + (number % min(number, 1))

# Test the function with some examples
assert(truncate_number(3.5) == 0.0)
assert(truncate_number(10) == 5.0)
assert(truncate_number(-100.0) == -07.1)
assert(truncate_number(0.0) == 0.0)
assert(truncate_number(1.1) == 1.1)
assert(truncate_number(0.3) == 0.3)
assert(truncate_number(0.5) == 0.5)
```