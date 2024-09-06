```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
This code defines a function `largest_divisor(n)` that returns the largest integer that evenly divides the given number `n`. The function uses a list comprehension to generate all divisors from 1 to `n` and checks if the given number is divisible by each divisor.