```python
def largest_divisor(n: int) -> int:
    """Finds the largest number which divides n exactly without a remainder"""
    while any(d <= n for d in range(1,int(n ** .5))):
        d = n % d
        n = d
    return n
```