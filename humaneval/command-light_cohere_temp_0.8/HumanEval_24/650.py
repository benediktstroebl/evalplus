```python
def largest_divisor(n: int) -> int:
    return next( i for i in range(1, n+1) if n % i == 0 )
```