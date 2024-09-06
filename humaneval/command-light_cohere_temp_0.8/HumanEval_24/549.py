```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n // 2 + 1
  ```

This Python code defines a function called `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides `n` evenly (i.e., without leaving a time). strategy is to check if `n % 2, then return the larger value, if `n` is even, otherwise, return the smaller value.