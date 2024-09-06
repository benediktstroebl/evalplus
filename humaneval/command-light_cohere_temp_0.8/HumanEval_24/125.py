```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if not any(n % i == 0))
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer `i` such that divides the number `n` evenly, where `i` is in the range from 1 to `n`. The `range(1, n+1)` provides all possible integers up to the value of `n`, and the `next()` function is used to generate the elements of the range one by one. The `if` statement is used to check if any of these numbers divide `n` evenly, and if not, it means that `n` is not divisible by any smaller number. The return statement returns the maximum integer that satisfies this condition.