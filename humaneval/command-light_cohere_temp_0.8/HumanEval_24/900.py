```python
def largest_divisor(n: int) -> int:
    return n if n < 2 else 1
    while n % 2 == 0:
        n //= 2
    return n
```