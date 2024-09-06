Here's a Python script with a self-contained function that finds the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next((i for i in range(1, n+1) if n % i == 0), n)
```

This code implements a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest divisor of `n`. The function uses a list comprehension to iterate from 1 to `n` and checks if `n` is divisible by each number using the modulo operator `%`. It returns the larger of these divisors or `n` itself if no divisors are found.