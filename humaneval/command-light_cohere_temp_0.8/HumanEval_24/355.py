```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)
```
This code defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest integer which divides the number `n` without a remainder. 

The function uses a `max` function with a generator expression to find the largest integer which does not leave a remainder when divided by `n`.