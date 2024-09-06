```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
This function returns the largest integer which evenly divides the given number n, i. the list of divisors are generated in ascending order, and the first element (the largest divisor) is returned using the `next()` function.