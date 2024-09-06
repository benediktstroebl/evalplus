```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This Python code defines a function named `largest_divisor` that takes an integer `n` as input and returns the largest integer that evenly divides `n`. This function uses an if-else statement to differentiate between cases where `n` is even and odd. The function then returns the result of the condition `n % 2 == 0` and returns `n + 1` in that case. Otherwise, it returns `n // 2`, indicating that `n` is odd and would be evenly divisible by 2. 

This code is a self-contained function that is entirely written in Python and does not require external functions or variables.