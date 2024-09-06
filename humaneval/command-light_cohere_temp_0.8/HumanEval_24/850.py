Here is a Python script with a self-contained function that finds the largest divisor of a given number:
```python
import math
def largest_divisor(n: int) -> int:
    """
    Returns largest number that divides n evenly, 
    smaller than n.
    """
    max_num = n -1
    while math.gcd(n, max_num) == 1:
        max_num -= 1
    return max_num
```