```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n - 1
```
This function returns the largest even divisor of the number n if the number is even, and returns the largest divisor of n - 1 if the number is odd.