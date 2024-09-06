Here is a Python script that contains a self-contained function that solves the problem:
```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if not any(n % i == 0))
```
This function generates all numbers from 1 to n, and then checks if any of them are divisors of n. The first number that satisfies the divisible with n, and returns it.