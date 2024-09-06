```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if n % i == 0)
```
The provided Python function, `largest_divisor`, uses the `next()` function and a generator expression to efficiently find the largest number that divides a given number `n` evenly. The function iterates through numbers from 1 to `n`, and checks if the remainder of `n` divided by each number is equal to 0. The `next()` function ensures that only the first occurrence of a number `i` is returned in the result, making it the largest divisor that satisfies the requirement.