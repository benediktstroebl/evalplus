Here's the self-contained Python script with a function that finds the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number smaller than n, that divides evenly"""
    while n % 2 == 0:
        n /= 2 
    return n
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n` without being equal to n. The function uses a technique of repeatedly dividing by 2 until the number is odd, at which point it stops looking for factors.