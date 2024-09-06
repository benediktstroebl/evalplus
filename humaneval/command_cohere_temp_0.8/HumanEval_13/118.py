```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b % a, a)
```

The `greatest_common_divisor` function uses Euclidean algorithm logic to find the greatest common divisor between two integers `a` and `b`. It is initialized with the two integers, and it returns the greatest common divisor between them. The base case is checking if any of the integers is 0, in which case it returns the other number (since no divisor of 0 is possible). The recursive step finds the gcd of the remainder of `b` divided by `a` and `a` itself. This continues until `b` is 0, at which point the current `a` is the GCD.