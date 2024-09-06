```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and d < n), 1)
``` 
This Python function, `largest_divisor`, takes an integer `n` as input and returns the largest integer that divides `n` without a remainder and is smaller than `n`. It uses the `next()` function with a generator expression `(d for d in range(1, n+1) if not n % d and d < n)`. This expression creates an infinite loop that generates all integers from 1 to `n`, checks if `d` divides `n` without a remainder, and is smaller than `n`, in that order. The `next()` function returns the generates the first such value in the list that meets these criteria.