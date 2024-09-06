Here's a self-contained Python script with a function that calculates the largest divisor of a given number n:
```python
import math
def largest_divisor(n: int) -> int:
    return math.sqrt(n) * math.sqrt(n + 1)
```
This script defines a function 'largest_divisor' which takes an integer n as input and returns the largest integer that divides n evenly (i.e.n is a scenario where can be used to find the maximum factor of n under the assumption that it's less than the original n. The function is based on the formula for the largest integer divisor of a given number n, which is equal to the square root of n times the square root of n + 1.