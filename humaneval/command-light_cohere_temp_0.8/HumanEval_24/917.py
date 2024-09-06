Here is a Python script that contains a self-contained function that finds the largest divisor of a given number:
```python
import math

def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    elif n <= 3:
        return math.max(2, 3)
    else:
        return 2 ** max(math.ceil(math.floor(math.sqrt(n)) -4))
```
This function utilizes specific cases for small numbers, and for larger numbers, it calculates the largest divisor using the square root calculation.