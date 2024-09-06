```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not any(n % d == 0)))
```
The code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer `divisible` by `n` but smaller than `n`. The function uses a generator expression with the `range` function and a list comprehension to find all the divisors from 1 to the number `n` using the condition `not any(n % d == 0)` that checks if the remainder of `n` divided by `d` is equal to 0. The `next` function returns the and is guaranteed to find the largest divisor, as it tests all numbers up to the given number.