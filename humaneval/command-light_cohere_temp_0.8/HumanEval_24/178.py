```python
def largest_divisor(n: int) -> int:
    return next( i for i in range(1, n+1) if all(j <= i for j in n//i) )
```