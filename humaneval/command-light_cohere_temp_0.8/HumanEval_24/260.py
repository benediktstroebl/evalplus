Here is a Python script with a self-contained function that finds the largest divisor of a given number:
```python
import math

def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that divides n exactly
    """
    return math.floor(math.sqrt(n) / 2)
```