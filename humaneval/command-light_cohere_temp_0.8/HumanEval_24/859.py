```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n - 1
```
This function takes an integer n as input and returns the largest integer that evenly divides n, smaller than n itself. It uses the dry division to find the largest divisor efficiently.