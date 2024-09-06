```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The algorithm is a recursive variation of the Euclidean algorithm for computing the greatest common divisor. It works by recursively setting the larger number as the dividend and the smaller number as the divisor. The recursion terminates when the divisor becomes 0, at which point the current dividend is the GCD of the two numbers.