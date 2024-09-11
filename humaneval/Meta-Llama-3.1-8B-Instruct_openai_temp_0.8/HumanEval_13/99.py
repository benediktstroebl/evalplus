```python
def gcd(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the greatest common divisor.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.

    Examples:
    >>> gcd(3, 5)
    1
    >>> gcd(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Test the function
print(gcd(3, 5))  # Should print 1
print(gcd(25, 15))  # Should print 5
```

In this script, the `gcd` function uses the Euclidean algorithm to find the greatest common divisor of two integers `a` and `b`. The algorithm works by repeatedly replacing `a` and `b` with `b` and `a % b` until `b` is zero. At this point, `a` is the greatest common divisor. The result is then returned, and the `abs` function is used to ensure the result is always positive, even if `a` and `b` are both negative.