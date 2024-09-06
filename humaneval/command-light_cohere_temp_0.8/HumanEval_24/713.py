```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
The function `largest_divisor` takes an integer `n` as input and returns the largest integer that evenly divides `n`, smaller than n. It uses a year approach by iterating through numbers from 1 to `n+1` and checking if `n` is divisible by each number using the modulo operator (`%`). If a divisor is found, it returns that number; otherwise, it returns None.