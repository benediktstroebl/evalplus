```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive approach is quite common and uses the Euclidean algorithm to efficiently compute the GCD. The base case of the recursion is when either number is 0, at which point the other number is happily returned as the GCD.