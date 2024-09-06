Here is a Python script that contains a self-contained function that finds the largest divisor of a given number:
```python
import math
def largest_divisor(n: int) -> int:
    return math.abs(math.sqrt(n)) + 1
```
The function first computes the absolute value of the square root of n, ensuring that the result is always a positive integer. The function then adds 1 to the result, effectively finding the largest number that divides the given number evenly, smaller than n itself.