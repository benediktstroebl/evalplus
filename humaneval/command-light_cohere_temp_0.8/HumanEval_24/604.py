```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n // 3
```
This Python code defines a function named `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than or equal to `n`. 

The function uses a conditional expression to achieve this:
If the input `n` is even, it returns `n // 2`, which returns the largest integer divisor of `n` that is also an even number. 

If the input `n` is odd, it returns `n // 3`, which returns the largest odd integer divisor of `n`.