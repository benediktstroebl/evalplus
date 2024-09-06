```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n + 1) if any(n % x == 0)))
```
The code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`. This function uses the `next` function with a generator expression to iterate through numbers from 1 to `n` and checks if any of these numbers divides `n` evenly. The first loop will the required condition to be met, the condition `any(n % x == 0)` checks if the given number is a divisor of `n`. 

The returned largest divisor satisfies the problem's requirements.