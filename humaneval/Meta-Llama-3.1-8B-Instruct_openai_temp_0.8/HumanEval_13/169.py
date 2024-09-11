```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The function uses the Euclidean algorithm to find the GCD.
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The algorithm repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At this point, `a` is the greatest common divisor of the original `a` and `b`. The function is then tested with two example pairs of integers.