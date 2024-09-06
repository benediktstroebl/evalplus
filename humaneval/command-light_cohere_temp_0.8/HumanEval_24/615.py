```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if all(n % x == 0)))
```
This function uses the list comprehension and the built-in function `next()` to find the largest number that divides the number `n` evenly without being equal to `n`. The test for `all(n % x == 0)` checks if the remainder of `n` divided by each number from `x = 1` to `n+1` is always zero. 
This function is self-contained and efficiently solves the problem of finding the largest number that divides a given number evenly.