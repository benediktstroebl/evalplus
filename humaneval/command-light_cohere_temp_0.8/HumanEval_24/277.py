Here's the self-contained Python script with a function that finds the largest divisor of a given number n:

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number divisible by n, smaller than n."""
    while n % 2 == 0:
        n -= 1
    return n
```

This code defines a function `largest_divisor(n)` that aims to find the largest integer that evenly divides the given number `n`. It uses a while loop until the number is even, then it finds the largest divisor by subtracting 1 until the number becomes odd.