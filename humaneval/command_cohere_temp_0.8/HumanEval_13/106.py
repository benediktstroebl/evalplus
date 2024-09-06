```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

The `greatest_common_divisor` function uses the Euclidean algorithm for computing the GCD. It replaces `b` with `b%a` in each iteration of the algorithm. This ensures that the remainder becomes smaller and approaches zero as the GCD is approached. It exploits the fact that the GCD operates on the remainder of successive divisions. 

This algorithm's time complexity is O(log(min(a, b))). It could benefit from optimization by applying the fast version of the modulo operator, such as the Montgomery Modular Multiplication algorithm. However, the basic version provided still fulfills the given problem requirements. 

This approach is efficient for larger values of `a` and `b` because it divides the smaller number by the larger number in each iteration, resulting in fewer iterations than other factorization methods.