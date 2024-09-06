Here's the self-contained Python function that solves the problem of finding the largest divisor of a given number: 

```python
def largest_divisor(n: int) -> int:
    return next((d for d in xrange(n) if not_divisible(d, n)), n)
def not_divisible(d: int, n: int) -> bool:
    return d * n > n
``` 

This function uses the `xrange` function to generate all the divisors of the number `n` and checks if the divisor divides the number evenly using the `not_divisible` function. The `not_divisible` function returns true if the divisor is greater than the number, which means it's not a divisor. 

Note that the return type of the `largest_divisor` function is int, even though the function returns the largest divisor as an argument. 

This code is self-contained and will solve the problem as requested.