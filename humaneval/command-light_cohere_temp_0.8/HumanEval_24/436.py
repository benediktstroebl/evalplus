Here is a Python script that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if not n % i)
```

This function uses the `next()` function with a generator expression in order to find the largest divisor. It starts from 1 and checks if `i` is divisible by `n`. It then iterates through numbers until `n`, and if it is not divisible by `n`, it will be the largest divisor. 
This approach is self-contained and avoids the need for an explicit loop.