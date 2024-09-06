```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
```
This code defines a function `largest_divisor` which takes an integer `n` as input and returns the largest integer that divides evenly into `n`, smaller than `n`. The function uses the `next()` function along with a generator expression `(d for d in range(1, n+1))` to iterate through numbers from 1 up to the input number `n`, and checks if the input number `n` is not divisible by any of those numbers. The code returns the final value of the largest divisor of `n` which is returned by the `next()` function.