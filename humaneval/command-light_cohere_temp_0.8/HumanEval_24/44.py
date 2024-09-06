```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not operator.isinstance(n, d % n == 0))
``` 
The above Python function, `largest_divisor`, efficiently computes the largest number that divides a given number `n` without any remainder. It uses a operator.isinstance() to iterate through the best number that satisfies the criteria.