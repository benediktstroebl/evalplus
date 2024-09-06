```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
This code defines a function named largest_divisor that takes an integer n as input and returns the largest integer that evenly divides n. The function uses a generator expression (d for d in range(1, n+1)) to iterate through numbers from 1 to n, checking if the current number d divides n evenly (i. If so, it returns that number as the largest divisor.