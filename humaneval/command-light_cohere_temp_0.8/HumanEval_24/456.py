```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not any(d % n == 0)))

# Test cases for the function
assert(largest_divisor(15) == 5)
assert(largest_divisor(20) == 5)
assert(largest_divisor(16) == 8)
assert(largest_divisor(10) == 2)
assert(largest_divisor(27) == 9)
assert(largest_divisor(19) == 13)
```