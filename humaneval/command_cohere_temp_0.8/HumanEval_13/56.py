```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The algorithm is a recursive variation of the Euclidean algorithm for computing the greatest common divisor. It works by the following steps:
1. If `b` is 0, then `a` is the GCD, so the function returns `a`.
2. If `b` is not 0, then the remainder of `a` divided by `b` is computed. This remainder is then passed to the function again, but in the argument `b`, and `a` is used as the new `b`.
3. The previous step is repeated until `b` becomes 0. At this point, the value of `a` is the GCD of the initial `a` and `b`.

The step 2 invokes the idea of using the remainder of the division as the input to the recursive call. This approach exploits the property that the GCD of two integers `a` and `b` is the same as the GCD of `b` and the remainder of `a` divided by `b`. 

The algorithm terminates when `b` becomes 0, at which point the current value of `a` is the GCD of the initial `a` and `b`.