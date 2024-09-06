```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(d % i == 0 for i in range(1, n)))) or n
```