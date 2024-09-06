```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), -1)
```
This Python function, `largest_divisor(n)`, uses the `next()` function with a generator expression to efficiently find the largest number that divides the given number `n` evenly, smaller than `n`. The function returns `-1` if no such number exists.