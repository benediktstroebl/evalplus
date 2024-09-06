```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if all(x % i == 0 for i in range(1, n))))
```
This code uses the Python next() function with a generator expression to efficiently find the largest divisor of the given number n, smaller than n, that divides it evenly. The function returns the N, which is the largest such divisor.