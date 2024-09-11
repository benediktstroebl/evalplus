```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap the values of a and b, and replace b with the remainder of a/b
        a, b = b, a % b
    
    # At this point, b is 0 and a is the GCD
    return abs(a)


# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input and returns their GCD. It also includes docstrings and example usage to demonstrate how to use the function.