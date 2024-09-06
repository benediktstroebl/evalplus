Here is a self-contained Python script with a function that solves the problem of finding the largest divisor of a given number:
```python
import math

def largest_divisor(n: int) -> int:
    if n < 2:
        return n
    return math.sqrt(n)
``` 
This script provides a function `largest_divisor` that calculates the largest divisor of the number n using the sqrt function, ensuring that the result is always greater than or equal to the input n.