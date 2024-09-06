```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient and is based on the following two observations:
1. To find the GCD of two integers `a` and `b`, it is enough to know the GCD of `b` and `a % b`.
2. If `b` is 0, then the GCD is `a`. 

The approach boils down to iteratively dividing the larger number by the smaller one, considering the remainder of the division operation as the larger number. This process continues until the remainder becomes 0, at which point the largest number starts to become the divisor.