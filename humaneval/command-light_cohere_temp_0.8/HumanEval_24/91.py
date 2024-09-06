```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not(n % d)) or n)
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides the number evenly (without leaving a remainder). The function uses a generator expression and the `next` function to iterate through the numbers from 1 to the number `n` while checking if the current number is a divisor of `n`.  It uses the condition `not(n % d)` to determine if the number divides `n` evenly.  The this specific test the checked against numbers from 1 up to the number `n` itself, ensuring that the result is always the largest number that satisfies the criteria.