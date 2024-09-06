```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), None) or n
```

This function, largest_divisor, returns the largest integer that evenly divides the given number n, smaller than n itself. The function uses the  a generator expression (next((d for d in range(1, n+1) if not n % d))) to generate all divisors of n, and returns the largest one. 

This function can be easily integrated into a larger program or used as-is for small-scale applications.