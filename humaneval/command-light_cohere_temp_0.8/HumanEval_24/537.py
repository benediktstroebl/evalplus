Here's the self-contained Python script with a function that solves the problem of finding the largest number divisor for a given number n:
```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if not any(n % i == 0))
```
This script defines a function `largest_divisor(n)` that uses a generator expression with a loop to iterate from 1 to `n` (inclusive). It checks if any divisor for n exists by testing if there's no remainder when dividing n by each integer in the range from 1 to n. 

This function effectively computes the largest divisor for n that is less than n and returns the divisor.