```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The GCD method uses Euclid's algorithm applied repeatedly to the two numbers until b becomes zero. At each step, the remainder of the division a / b gives the same remainder that a would leave when divided by the actual GCD, so the algorithm gradually reduces the problem to finding the remainder of a / b when b is zero, which is equal to a.

This algorithm is very efficient and is able to compute the GCD in linear time without requiring any nested or recursive calls.