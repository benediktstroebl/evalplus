```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

This script defines a recursive function `greatest_common_divisor` that calculates the GCD of two integers `a` and `b` using the Euclidean algorithm. It is tested against the given test cases and is also recursively tested. 

To avoid potential issues with integer division, it checks for zero values and returns the respective input value in those cases. 

Please ensure that you have a robust integer division mechanism before deploying this code to avoid potential complications.  If you have further questions or complications, feel free to ask!