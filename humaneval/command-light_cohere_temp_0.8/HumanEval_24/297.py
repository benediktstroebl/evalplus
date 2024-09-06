```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), n)
``` 
This code defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`. This function utilizes the `next()` function and a generator expression `(d for d in range(1, n+1) if not n % d), n)` to iterate through all numbers from 1 to `n` (inclusive) while checking if the current number divides `n` evenly. The first element that will always be `n`, so it returns the largest number smaller than `n` as the result.