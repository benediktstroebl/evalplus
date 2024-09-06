```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and d != 1),)
```
This code provides a solution to the problem you provided earlier.  It also utilizes the provides a function that calculates the largest divisor of a given number n, ensuring that the divisor is smaller than n.