```python
def largest_divisor(n: int) -> int:
    return n // max([1] + [n % d for d in range(2, int(n**0.5)])
```

Here is the breakdown:
- The function `largest_divisor` takes one argument `n: int` which is the number to find the largest divisor for.
- The function uses the built-in function `max` to find the maximum of the list `[1] + [n % d for d in range(2, n**0.5)]`. This largest number that divides `n` evenly and is less than `n`.