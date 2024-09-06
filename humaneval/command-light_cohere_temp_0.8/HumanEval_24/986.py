```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if not n % i)
```
This Python function, `largest_divisor`, is designed to find the largest integer that evenly divides a given number `n`. 

It utilizes a generator expression with the `next()` function and the `range(1, n+1)` sequence to iterate through numbers from 1 up to the target number `n`. 

This approach ensures that the function returns the largest such divisor, which is crucial for solving problems related to finding divisors efficiently. 

The function follows a straightforward algorithm, and it efficiently fulfills the purpose of finding the largest divisor for a given number `n`.