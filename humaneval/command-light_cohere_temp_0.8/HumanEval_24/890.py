```python
def largest_divisor(n: int) -> int:
    return n // max(1, n // i for i in range(2, int(n**0.5)))
```
This function computes the largest divisor of n which divides n exactly, and ensures that the result is less than n.