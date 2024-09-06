```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not any(n % d)))
``` 
This code defines a function `largest_divisor` that finds the largest number which divides the given number `n` without a remainder. It uses the final values and the next function to iterate over numbers from 1 up, and the condition `not any(n % d)` checks if the divisor doesn't result in a remainder when dividing `n` by it. The returned value of the maximum divisor found during the loop, which satisfies the specified problem.