```python
def largest_divisor(n: int) -> int:
    return (n // 2) + 1
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`, meaning the largest number `k` such that `k * i = n` for all integers `i` from 0 to `n/2`. The function essentially returns the number `n-//2 + 1` which ensures the largest number is greater than `n` but divides evenly into `n`.