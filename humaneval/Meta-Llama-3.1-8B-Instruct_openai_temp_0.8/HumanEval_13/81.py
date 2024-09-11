```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    
    The Euclidean algorithm is used to find the GCD of two numbers.
    It works by continuously replacing 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b',
    until 'b' is zero. At that point, 'a' is the GCD.
    
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

In this script, the `greatest_common_divisor` function uses the Euclidean algorithm to find the GCD of two integers `a` and `b`. The `while` loop continuously replaces `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD. The `abs` function is used to ensure the GCD is always positive, even if the input numbers are negative. The script then tests the function with the provided examples.