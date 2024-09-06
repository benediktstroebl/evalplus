Here is a self-contained Python script that defines a function `largest_divisor(n: int) -> int` that finds the largest number that divides the input number evenly, smaller than the input:
```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0), n)
```
The function returns the largest integer that evenly divides the given number `n`.  It uses a list comprehension with a generator expression to find the largest such divisor.  The generator expression returns integers from 1 to `n` (inclusive) and tests if the remainder of `n` divided by each number is equal to 0, which means that it divides evenly.  The result above a most efficient algorithm for finding the largest divisor of a number.