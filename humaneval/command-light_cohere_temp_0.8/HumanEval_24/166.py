```python
def largest_divisor(n: int) -> int:
    return n // max([i for i in range(1, n + 1) if n % i == 0])
```
This function uses the `max` function with a generator expression to find the largest integer that divides the number n exactly or evenly. It returns the ** integer that results from the above process.