```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```

This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer `k` such that `k` divides `n` evenly. The function uses theessential approach that it iterates through numbers from 1 to `n+1` and checks if `n` is divisible by each number using the modulo operator `%`. The `next()` function is used to retrieve the next number in the sequence. This implementation efficiently finds the maximum divisor for a given number `n`.