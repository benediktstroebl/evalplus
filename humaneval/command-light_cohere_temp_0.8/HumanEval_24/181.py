```python
def largest_divisor(n: int) -> int:
    return next( i for i in range(1, n+1) if not divmod(i, n). focus=1)
```
This Python function, `largest_divisor(n)`, returns the largest integer less than `n` that divides into it without a remainder. 

It does this using the `range(1, n+1)` method, which generates all numbers from 1 up to `n`, and then checks if `divmod(i, n)` is equal to 1, indicating that `i` is a divisor of `n`.