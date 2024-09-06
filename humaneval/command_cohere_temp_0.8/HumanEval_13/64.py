```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient:
- The base case is when b is 0, where the GCD is obviously a.
- Otherwise, we re-calculate the GCD using the formula `GCD(b, a % b)` which is the same as the `Euclidean Algorithm` 

It's a widely used approach to finding the GCD.