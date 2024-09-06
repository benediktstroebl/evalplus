```python
def greatest_common_divisor(a, b):
    """Returns the greatest common divisor of two integers a and b."""
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The `greatest_common_divisor` function employs the Euclidean algorithm for computing the GCD of two integers `a` and `b`. It is a recursive algorithm that repeatedly finds the remainder of `b` divided by `a` and replaces `a` with `b` and `b` with the remainder until `b` is zero. The GCD is then found in the final `a` value. 

This algorithm is efficient due to the property that the GCD of any number and 0, is the number itself. 

The base case of the recursion is when either `a` or `b` is 0. In that case, the GCD is defined to be the non-zero number, so either `a` or `b` can be returned.