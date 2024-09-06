Here is a self-contained Python script that solves the problem of finding the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next((i for i in range(1, n+1) if not n % i), n)
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n` using the `next` function.  The `next` function generates the largest number that does not leave remainder when dividing `n` and returns the number.