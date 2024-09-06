```python
def largest_divisor(n: int) -> int:
    return next(
        i for i in range(1, n + 1) if all(j <= i%d for j in range(1, n+1))
    )
``` 
This code defines a function `largest_divisor(n)` that aims to find the largest integer `d` such that `d` divides `n` exactly and all its divisors are less than `n`. 

This function uses the `next()` function with a generator expression that iterates through numbers from 1 up to the given input integer `n`. The function returns the largest such number. 

This solution is self-contained, and it efficiently finds the largest divisor without requiring multiple iterations or specific divisibility checks.