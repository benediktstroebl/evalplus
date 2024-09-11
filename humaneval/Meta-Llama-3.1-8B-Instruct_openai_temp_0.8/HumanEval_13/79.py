```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ 
    Return the greatest common divisor of two integers a and b.
    
    The Greatest Common Divisor (GCD) of two integers is the largest integer that divides both numbers without leaving a remainder.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    
    Example:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

In this script, the `greatest_common_divisor` function uses the Euclidean algorithm to find the greatest common divisor of two integers. This algorithm repeatedly replaces `a` and `b` with `b` and `a % b`, respectively, until `b` is zero. At this point, `a` is the greatest common divisor. The `abs` function is used to ensure the result is always positive.