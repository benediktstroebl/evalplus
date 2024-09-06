Here's the self-contained Python function that finds the largest divisor of a given number n: 

```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if n % i == 0)
```

This function iterates over numbers from 1 to n, and returns the largest divisor found.  It uses the can be used as a self-contained solution for the problem statement.