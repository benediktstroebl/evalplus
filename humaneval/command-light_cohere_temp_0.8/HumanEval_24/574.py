```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n - 1
```
This function returns the largest integer which evenly divides the given number, smaller than the given number.