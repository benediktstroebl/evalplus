```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This code defines a function `largest_divisor` that calculates the largest divisor of a given integer `n`. The function uses the condition to check if the number is even or odd, and returns the appropriate value accordingly, ensuring the largest divisor is always greater than or equal to `n`.