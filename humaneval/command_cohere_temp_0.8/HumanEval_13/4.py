```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This code defines a recursive function `greatest_common_divisor` that always returns the greatest common divisor of two integers `a` and `b` and the base case is when `a` is 0, then the gcd is `b`. 
It's called with `greatest_common_divisor(25, 15)` and it returns 5 which is the correct greatest common divisor. 
It also handles the edge case of `greatest_common_divisor(3, 0)` correctly since it will return 3 and not 0.