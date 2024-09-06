```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test the function with various inputs
assert(largest_divisor(15) == 5)
assert(largest_divisor(10) == 5)
assert(largest_divisor(12) == 4)
assert(largest_divisor(27) == 9)
assert(largest_divisor(60) == 10)
assert(largest_divisor(72) == 12)
assert(largest_divisor(90) == 45)
```