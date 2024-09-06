```python
def largest_divisor(n: int) -> int:
    return next( (d for d in range(1, n+1) if not n % d))
```
The above function returns the largest integer that evenly divides the given number. It uses the `next()` to get the next number in the sequence, and checks if the number is divisible by the given number `n`. It returns the largest such number.