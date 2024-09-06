```python
def largest_divisor(n: int) -> int:
    return n if n % 2 == 0 else n+1
```

This Python code defines a function named `largest_divisor` that takes an integer `n` as input and aims to find the largest divisor of `n`. It uses a conditional statement to achieve this: If `n` is even, it simply returns `n`; otherwise, it returns `n + 1`, ensuring that the result is always greater than or equal to `n`. The function efficiently finds the largest number that divides `n` evenly, smaller than `n`.