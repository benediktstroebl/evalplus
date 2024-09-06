```python
def largest_divisor(n: int) -> int:
    return next( (d for d in range(1, n+1) if n % d == 0))
```
The function returns the largest number that evenly divides the given number, smaller than the number n. The function uses the first for loop to generate all numbers from 1 up to n, and checks if the given number is divisible by any of them. The next(generator) simplifies this process.