```python
def largest_divisor(n: int) -> int:
    return (n-1) if n % 2 == 0 else n + 1  # using divisibility principles
```
This function returns the largest integer which evenly divides the given number without any remainder.