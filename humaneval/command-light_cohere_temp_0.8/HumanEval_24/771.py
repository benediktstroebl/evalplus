```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not num_divisible(n, d))) or n

def num_divisible(n: int, d: int) -> bool:
    return n % d == 0
```
The provided code defines a Python function `largest_divisor(n)` that calculates and returns the largest divisor of the given number `n`. The `num_divisible(n, d)` function checks whether a given divisor `d` can divide `n` without leaving a remainder, using the modulo operator `%`. The function returns `True` if the divisor is a factor of `n`, indicating that `n` is divisible by `d`.