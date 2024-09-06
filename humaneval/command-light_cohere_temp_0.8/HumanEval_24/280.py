```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
This function takes an integer n and returns the largest integer which divides n exactly. It uses the  the if n is divisible by any integer less than n, that means it's not divisible by any integer greater than it, so we can directly return that smaller integer.