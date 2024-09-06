```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
The function returns the largest integer which evenly divides the number n, ensuring that the result is strictly greater than n.