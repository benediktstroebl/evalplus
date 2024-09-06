Here is a Python script with a self-contained function that solves the problem of finding the largest number that divides a given number evenly, smaller than n:
```python
import math

def largest_divisor(n: int) -> int:
    if n < 2:
        return n
    return math.sqrt(n - (math.div same_as_ n % (n-1))
``` 
The function checks for the base case where n is less than 2 and returns n itself. If n is greater than 2, the function uses the formula to find the largest integer that divides n evenly. It then uses the formula to calculate the largest such number, which involves squaring the integer n and subtracting 1 from n.