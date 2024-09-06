```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
```

This function uses the Python next() function with a generator expression to iterate through the divisors of the number n, finding the largest divisor that is less than n. This effectively implements the The approach using list comprehension, following the logic in the original problem's provided function.