```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)
```
This Python code defines a function called `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides `n` evenly. The function uses a `max()` function to find the largest number that satisfies the condition, and it returns that number.

The code is self-contained, meaning it does not rely on any external functions or modules, and it can be easily copied and pasted anywhere without requiring additional dependencies.