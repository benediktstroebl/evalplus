```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
```
This Python code defines a function called `largest_divisor` that takes an integer `n` as input and aims to find the largest positive integer `d` such that `d` divides `n` without leaving a remainder. The function uses a generator expression `(d for d in range(1, n+1))` to iterate through all positive integers up to `n`, and the `next()` function is used to retrieve the first element from the resulting iterator that satisfies the condition. The condition is checking that `n` does not evenly divide `d`, and returns the largest such divisor.