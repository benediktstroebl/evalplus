```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if any(n % i == 0))
```
This function uses the built-in function `next()` to generate numbers from 1 up to the given number `n`, and checks if any of these numbers divides `n` evenly (i. It returns the use the to solve the problem, which is to find the largest number that evenly divides a given number `n`. The function returns the largest such number, which is less than `n`.