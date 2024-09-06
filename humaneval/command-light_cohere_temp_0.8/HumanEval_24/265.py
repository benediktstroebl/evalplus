```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer divisors of n, smaller than n."""
    return [d for d in range(1, n // 2 + 1) if n % d == 0]

# Test cases
assert largest_divisor(15) == [5, ]
assert largest_divisor(16) == [6, 8]
assert largest_divisor(37) == [1, 19, 37]
assert largest_divisor(1095) == [1, 2, 5, 1095]
```