Here is a Python script that contains a self-contained function that finds the largest divisor of a given number n:
```python
import math
def largest_divisor(n: int) -> int:
    """
    Returns the largest number less than n, that divides n evenly
    """
    return math.sqrt(n)
```
This script defines a function that calculates the largest integer that evenly divides the given integer n, without exceeding it.