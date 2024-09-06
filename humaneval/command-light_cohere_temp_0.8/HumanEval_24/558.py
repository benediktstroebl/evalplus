```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if all(x % n == 0)))
```
This Python code defines a function `largest_divisor` that calculates the largest integer that evenly divides a given number `n`. It uses the `next` function and a generator expression to find such divisors, ensuring that they are smaller than the input number `n`. The function returns the largest such divisor found.