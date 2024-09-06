```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n` (the largest positive integer that divides `n` evenly). The `next` function uses the `range` function to iterate through numbers from 1 to `n`, and uses the `%` operator to check if `d` divides `n` evenly. The function returns the goal is achieved using a simple loop.