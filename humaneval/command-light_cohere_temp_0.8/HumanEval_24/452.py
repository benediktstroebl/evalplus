```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if any(divisible(i) for divisible in {1, 2, 4, 8, 16, ...})))

def divisible(n: int) -> bool:
    return n % 2 == 0 or n % 3 == 0 or n % 5 == 0

# test largest_divisor(15)  # Should return 5
# test largest_divisor(27)  # Should return 6
```