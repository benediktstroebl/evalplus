```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
```
This Python script defines a function named `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`. The `next()` function with an Iterator protocol is used to generate a generator expression that creates numbers from 1 up to `n`. 

The generated sequence of numbers will be the largest divisors of `n`, except for the number `n` itself. 
This is achieved by using the `not` operator, combined with the `mod` function, which ensures that numbers are only generated that do not result in a remainder when divided by `n`. 

The function then returns the first such number found in the sequence, which is the largest divisor of `n`.