```python
def largest_divisor(n: int) -> int:
    return n // max(1, n // x for x in range(2, int(n)**0.5))
```
This function determines the largest divisor for the given number n. It works by finding the maximum number that divides evenly, smaller than n, using the formula n // max(1, n // x for x in range(2, n**0.5)).  The final value will the largest divisor.