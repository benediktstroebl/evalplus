```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if any(x % i == 0 for i in range(1, n)) == True))
```
This Python function `largest_divisor` takes an integer `n` as input and returns the largest integer that evenly divides `n`. This is achieved using the `next()` function and a generator expression, which iterates over numbers from 1 up to the given number `n`. The function then checks if any of these divisors are equal to 0, indicating that they evenly divide `n`.