Here is a self-contained Python script that defines a function to find the largest divisor of a given number:
```python
import math
def largest_divisor(n: int) -> int:
    return math.sqrt(n) + 1
```
This script provides a function called `largest_divisor` that calculates the largest integer dividing a given number `n` evenly, ensuring that the result is greater than or equal to `n`.  The function uses the `math.sqrt()` function to find the largest integer less than the square root of `n` and adding 1 to it, ensuring the result is greater than `n`.  This is a self-contained solution to the problem of finding the largest divisor of a given number.