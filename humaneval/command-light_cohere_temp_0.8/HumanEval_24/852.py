```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not any(n % d)))
```
This code provides a solution for finding the largest divisor of a given number.  It uses a large loop and a conditional check to identify and return the largest divisor.