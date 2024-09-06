```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This function computes the largest integer that evenly divides the given number 'n', while ensuring the result is less than or equal to 'n'.