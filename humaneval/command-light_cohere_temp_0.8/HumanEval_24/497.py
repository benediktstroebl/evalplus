Here is a Python script with a self-contained function that solves the problem of finding the largest divisor of a given number:
```python
import math
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    lcm = n // math.sqrt(n) * math.sqrt(n)
    divisor = int(math.ceil(n / lcm))
    for i in range(2, math. divisor):
        if n % divisor == 0:
        return divisor
    return -1
```