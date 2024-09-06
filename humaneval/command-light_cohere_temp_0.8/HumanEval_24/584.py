Here is a Python script with a self-contained function that solves the problem of finding the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return n // max([1] + 4 * i for i in range(1, int(n**0.5)))
```

This function uses the `math.range` algorithm with a `max` function to find the largest number that divides the given number `n` evenly, smaller than `n`.