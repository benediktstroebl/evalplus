```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(n % d == 0)))
```
This function uses the next() function with a generator expression to generate numbers from 1 to n. It then checks if all of these numbers divide evenly into n, using the all() function. The first number that does not divide evenly into n is returned as the largest divisor.