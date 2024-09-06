```python
def largest_divisor(n: int) -> int:
    return n if n % 2 == 0 else n+1
```
This code defines a function `largest_divisor` which returns the largest integer divisor of a given number `n` (excluding `n` itself). The function utilizes a conditional check to determine whether `n` is even or odd, and then returns the larger of the two values.