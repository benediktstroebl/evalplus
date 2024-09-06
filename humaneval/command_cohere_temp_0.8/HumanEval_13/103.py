```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a recursive function `greatest_common_divisor` that takes two integers `a` and `b` as inputs. It aims to find the greatest common divisor (GCD) of these two numbers. The base case of the recursion is when `b` is 0, in which case the GCD is `a`. Otherwise, the function recursively calls itself with the arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. This process continues until `b` becomes 0, at which point the recursion unwinds and the final GCD is computed.