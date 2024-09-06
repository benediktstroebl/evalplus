```python
def largest_divisor(n: int) -> int:
    return n if n > 1 else 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i
    return n
```