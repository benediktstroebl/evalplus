```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if any(n % i == 0))
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`, smaller than `n`. This is a self-contained solution to find the largest divisor. The function uses a simple list comprehension to generate numbers from 1 up to the given number `n`, and uses the `any` function to check if any of these numbers divides `n` evenly.