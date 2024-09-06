```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not evenly_divisible(n, d)), n)

def evenly_divisible(n: int, d: int) -> bool:
    return n % d == 0 and d <= n
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n`, which is smaller than `n`. The function uses a generator expression to find all divisors of `n` and returns the largest one that isn't `n`.  This ensures that the answer is indeed the largest divisor that divides `n` evenly.