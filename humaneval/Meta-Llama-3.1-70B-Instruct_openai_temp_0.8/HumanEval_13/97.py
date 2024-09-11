```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm to find the GCD.
    
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b`. The function uses the Euclidean algorithm, which repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` is 0. At that point, `a` is the GCD. The function returns the absolute value of `a` to ensure a non-negative result.

You can run this script to test the `greatest_common_divisor` function with different inputs.