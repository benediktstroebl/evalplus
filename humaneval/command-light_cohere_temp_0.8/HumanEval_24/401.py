```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test cases
assert largest_divisor(1) == 1, "Invalid input - should return 1"
assert largest_divisor(2) == 2, "Invalid input - should return 2"
assert largest_divisor(3) == 3, "Invalid input - should return 3"
assert largest_divisor(5) == 5, "Invalid input - should return 5"
assert largest_divisor(10) == 5, "Invalid input - should return 5"
assert largest_divisor(13) == 5, "Invalid input - should return 5"
assert largest_divisor(16) == 4, "Invalid input - should return 4"
```