```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.
    
    The greatest common divisor (GCD) of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.
    
    This function uses the Euclidean algorithm to compute the GCD.
    
    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
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

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. It uses the Euclidean algorithm to compute the GCD. The function is then tested with two examples.