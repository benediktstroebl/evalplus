```python
def largest_divisor(n: int) -> int:
    return n // max([1] + 4, 1)

# Test cases
assert largest_divisor(15) == 5
assert largest_divisor(27) == 3
assert largest_divisor(12) == 4
assert largest_divisor(4) == 4
assert largest_divisor(1) == 1
assert largest_divisor(0) == 0
```