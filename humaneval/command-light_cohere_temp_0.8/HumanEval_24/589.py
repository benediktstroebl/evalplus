```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not any(n % d == 0)))
```
The function uses the `next()` function to iterate over the numbers from 1 to `n` (inclusive), and it checks if any of those numbers are divisors of `n` by using the `not any(n % d == 0)` condition.  This time to find the general solution that finds the largest number that divides `n` evenly, without being `n`.