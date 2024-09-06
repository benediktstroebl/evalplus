Here's a self-contained Python function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
```
This function returns the largest integer that evenly divides the given number, smaller than the input n.