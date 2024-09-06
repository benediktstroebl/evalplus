```python
def largest_divisor(n: int) -> int:
    return next(x for x in range(1, n+1) if not any(n % x == 0))
```
This Python function, largest_divisor(n), returns the largest integer that evenly divides the given number n, without being equal to n itself. It uses the approach by iterating through numbers from 1 to n+1, and using the built-in function next() to generate the next integer in the sequence. The condition for not dividing evenly is checked using the statement if not any(n % x == 0), which returns True if no common factors are found. The function then returns the this next discovered number.