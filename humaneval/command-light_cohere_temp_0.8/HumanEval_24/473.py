Here is a Python script with a self-contained function that solves the problem of finding the largest divisor of a given number:
```python
import math
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer which divides the given number evenly
    """
    if n < 2:
        return n
    else:
        return math.findallone(n, (1) + 2)
``` 
This script has a function named `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides the given number evenly. The function uses theator's built-in function `math.findall` to find the huge prime factors of `n`, starting from the smallest one.