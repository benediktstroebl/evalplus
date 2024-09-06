Here is a Python script with a self-contained function that solves the problem of finding the largest divisor of a given number:
```python
import math
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    return math.sqrt(n) // math.sqrt(n+
    largest_divisor(n) - 1)
```
The function returns the largest integer that divides the given number evenly, smaller than the given number. This is a most efficient way of finding the largest divisor, which is to find the square root of the given number and then subtract 1.