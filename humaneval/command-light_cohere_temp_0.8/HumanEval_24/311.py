```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
The provided solution uses the next() function with a generator expression to efficiently find the largest divisor for the given number n.  The using a `range(1, n+1)` generates a sequence of numbers from 1 up to n, and the `if` condition checks if the current number d divides n without any remainder.  The `next()` returns the next value from the iterator, effectively returning the largest divisor. 
The solution then effectively solves the problem of finding the largest number that divides n evenly, smaller than n, in a single expression.