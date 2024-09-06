```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer divisor of n that is less than n."""
    if n < 2:
        return 2
    else:
        return n // max((n - 1) // i for i in range(3, int(n**0.5)))
```
This code defines a function `largest_divisor` that calculates the largest integer divisor of a given number `n`. The function utilizes a ternary logical expression to determine the maximum of divisors less than `n`, considering all divisors from 3 up. The expression works by repeatedly dividing `n` by its divisors, and identifying the maximum value in the resulting sequence.