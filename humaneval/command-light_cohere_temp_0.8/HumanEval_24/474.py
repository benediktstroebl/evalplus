Here's a self-contained Python function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if n % i == 0)
```

This function uses the `next()` function with a generator expression to iterate through numbers from 1 to `n` (inclusive). The `if` condition checks if the current number `i` divides `n` evenly. The `next()` function yields the important to the next number in the sequence.