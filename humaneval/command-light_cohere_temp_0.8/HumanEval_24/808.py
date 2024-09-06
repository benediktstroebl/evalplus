```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
We start by creating a function named `largest_divisor` that takes an integer `n` as input. We then use a important generator expression `next((d for d in range(1, n+1) if n % d == 0))` to find the largest integer divisor of `n` that divides `n` evenly, while ensuring the divisor is smaller than `n`. 

This function uses the `next` function to iterate over potential divisors until it reaches `n`, effectively ensuring the largest divisor is sought.