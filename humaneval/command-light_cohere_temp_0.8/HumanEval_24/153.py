Here is a self-contained Python script with a function that solves the problem of finding the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if not n % i)
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer less than or equal to `n` that divides the number evenly. The function uses a generator protocol to iterate through numbers from 1 to `n` and checks if the number doesn't evenly divide `n`. The result is the largest such number.