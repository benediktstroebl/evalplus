```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The algorithm is a recursive variation of the Euclidean algorithm for computing the greatest common divisor. It exploits the fact that the GCD of two numbers `a` and `b` is the same as the GCD of `b` and `a % b`. When `b` is 0, the GCD is `a`. 

It's a concise approach that improves efficiency by cutting down the number of recursive calls.