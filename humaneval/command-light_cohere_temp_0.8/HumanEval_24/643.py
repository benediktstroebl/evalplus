```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n + 1) if all(x % n == 0)))
```
This Python code defines a function called `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`. This function employs a generator expression and the `all` function to achieve this.