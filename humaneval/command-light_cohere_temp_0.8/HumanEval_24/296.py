```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if all(n % i == 0))
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`.  It uses a list comprehension with a generator expression `(i for i in range(1, n + 1))` to iterate through numbers from 1 up to `n`, and checks if `all(n % i == 0)` to see if `i` is a divisor of `n`. The function returns the first such number found in the list comprehension.