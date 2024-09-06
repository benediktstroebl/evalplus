Here is a Python script with a self-contained function that solves the problem of finding the largest divisor of a given number:
```python
import math

def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    m = math.ceil(n / 2)
    return m
```

This function uses the `math` module to calculate the largest even divisor of the number n using the `ceil` function, which returns the largest number less than or equal to the input.

You can use this function with any positive integer number to find the largest divisor.