```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

The `greatest_common_divisor` function uses the Euclidean algorithm for computing the GCD. It refines the algorithm from earlier by immediately returning `a` if it is 0, since `b` is then the GCD. 

This is a more efficient approach that also aligns with a recursive call stack, where each step brings you closer to finding the divisor. 

It is also worth noting that for performance-critical applications, Python's built-in `math` module provides a C-based `gcd` function that outperforms Python's native `math.gcd` in terms of speed.