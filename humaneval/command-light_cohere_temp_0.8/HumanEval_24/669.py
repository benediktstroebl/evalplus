```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if all(n % i == 0))
```
This Python function, `largest_divisor`, takes an integer `n` as input and returns the largest integer that evenly divides `n`, smaller than `n`. This is achieved through a generator expression that iterates through numbers from 1 to `n` using the `range()` function. The `all()` function is then used with `n % i` to check if `i` divides `n` evenly. 
 ensures that only the numbers that evenly divide `n` are considered as potential divisors, and the first such number encountered is returned.