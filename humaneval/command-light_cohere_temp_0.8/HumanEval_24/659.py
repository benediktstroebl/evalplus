```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if not n % i)
```
This Python function named `largest_divisor` takes an integer `n` as input and returns the largest integer that divides evenly into `n`, i.e., the goals for divisors less than `n`. The function employs a generator expression with the `next` function and the `range` function to generate all numbers from 1 to `n` (inclusive). The `if` condition is used to check if the current number `i` is divisible by `n`, and if it is not, then the function returns `i`.  The function then returns the largest such number found, which is guaranteed to be less than `n`.