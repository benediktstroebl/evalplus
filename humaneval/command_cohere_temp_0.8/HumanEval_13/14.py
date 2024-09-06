```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The logic of this approach is to use the Euclidean algorithm with the auxiliary function. The algorithm consists of the following steps:
1. If `b` is 0, then `a` is the GCD, so the algorithm stops.
2. If `b` is not 0, then the remainder of the division of `a` by `b` is computed.
3. The GCD is computed repeatedly using the auxiliary function, where `a` is replaced by `b`, and `b` is replaced by the remainder.

The algorithm terminates because the remainder of the division becomes 0, which means that `a` and `b` are divisible by the GCD. 

This approach has a time complexity of `O(log(min(a, b)))` and is efficient compared to other algorithms.