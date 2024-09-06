```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This function, named `largest_divisor`, takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than or equal to `n`. It employs the logic that if a number is even, the largest divisor would be `2` itself, and if the number is odd, the largest divisor would be `n + 1`.