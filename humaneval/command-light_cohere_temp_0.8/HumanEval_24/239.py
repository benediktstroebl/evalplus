Here is a Python script that contains a self-contained function that calculates the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```

This function tests out divisors from 1 to the given number n, and returns the largest divisor found.