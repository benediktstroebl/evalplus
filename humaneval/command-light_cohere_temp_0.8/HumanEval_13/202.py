Here's a Python script that includes the function `greatest_common_divisor`, which calculates the greatest common divisor of two integers `a` and `b` passed as arguments:
```python 
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of two integers a and b. """
   
    for i in range(1, max(a, b) // 2):
        if a % i == 0 and b % i == 0:
            return i
    return 0
```
The `greatest_common_divisor` function calculates the greatest common divisor of two integers `a` and `b` by iteratively testing divisibility up to the square root of the smaller number, returning the first positive value for which both numbers are divisible.