Here is a self-contained Python script that defines a function `largest_divisor` solving the problem you provided:
```python
import math
def largest_divisor(n: int) -> int:
    """ Returns the largest number which divides n evenly"""
    while n % 2 == 0:
        n -= 1
    return math.sqrt(n)
```
This function uses a while loop to find the largest number that evenly divides the given number `n`. It removes the even divisor from `n` until the number becomes odd.  The largest odd divisor is the square root of the remaining number.