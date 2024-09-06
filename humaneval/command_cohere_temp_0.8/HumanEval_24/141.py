```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function `largest_divisor(n)` takes a number `n` as input and iterates through all numbers from 1 to `n` (inclusive). During each iteration, it checks if the current number `i` can divide `n` evenly. If `n` is divisible by `i` with no remainder, it means that `i` is a factor of `n`. The function returns the largest such number `i` that divides `n` evenly, which means the largest divisor of `n` that is also smaller than `n`.