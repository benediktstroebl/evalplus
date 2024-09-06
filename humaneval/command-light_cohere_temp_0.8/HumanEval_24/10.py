```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), -1)
```
This function returns the largest divisor of the number n that is less than n itself, which ensures the value is divisible. 
It uses the next function to iterate through divisors of n, checks for each divisor if it's not divisible by n, and returns -1 if no such divisors are found after exhausting the loop.