Here is a Python script with a self-contained function that solves the problem of finding the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer that divides the given number evenly"""
    while n % 2 == 0:
        n /= 2
    return n
```

This function uses a while loop until the given number becomes even. It then returns the