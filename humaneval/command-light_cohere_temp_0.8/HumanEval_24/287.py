```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
```
The provided code defines a function named `largest_divisor` that takes an integer `n` as input and returns the largest integer which divides the given number evenly. It uses the goal is generating a list of divisors from 1 to n, and then uses the `next()` function with a generator expression `(d for d in range(1, n + 1))` to return the first element of the list that satisfies the condition `n % d == 0`.