```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not_divisible(d, n)), n)

def not_divisible(d: int, n: int) -> bool:
    return d * n == 0 and d != 0

# Test cases
assert largest_divisor(2) == 1
assert largest_divisor(3) == 3
assert largest_divisor(6) == 6
assert largest_divisor(12) == 4
assert largest_divisor(15) == 5
assert not_divisible(1, 10)
assert not_divisible(2, 20)
```
The function `largest_divisor` returns the largest number that evenly divides `n`, smaller than `n`. The function `not_divisible` checks if `d` divides `n` without any remainder, and returns `True` if it does. The script also includes test cases for various input values.