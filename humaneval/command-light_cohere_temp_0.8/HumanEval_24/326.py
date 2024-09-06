Here is a self-contained Python script that solves the problem of finding the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next((d for d in x if d > 0 and n % d == 0), n)
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n`. It uses a generator expression with the `next` function and a list comprehension to iterate over all divisors of `n`, including negative numbers and numbers that are equal to `n`, and returns the largest divisor.