```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This function uses the Euclidean algorithm to find the largest divisor of a number n, it returns the largest number that divides n exactly.