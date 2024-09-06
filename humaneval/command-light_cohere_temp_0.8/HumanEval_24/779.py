Here is a self-contained Python script that solves the problem of finding the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if n % i == 0)
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n`. The function uses a generator expression with the `next()` function and the `range(1, n+1)` to generate all numbers from 1 to `n` and checks if the remainder of `n` divided by each number is equal to 0.

The `largest_divisor` function can be used to find the largest divisor of any given number by passing the number as an argument to the function.