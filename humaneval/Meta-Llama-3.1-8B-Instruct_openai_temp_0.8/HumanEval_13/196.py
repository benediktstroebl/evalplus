```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    The greatest common divisor (GCD) of two integers a and b is the largest positive integer that divides both numbers without leaving a remainder.
    
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

    # Ensure a and b are integers
    a = int(a)
    b = int(b)

    while b!= 0:
        # Use the Euclidean algorithm to find the GCD
        a, b = b, a % b

    return abs(a)


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The Euclidean algorithm works by repeatedly replacing 'a' and 'b' with 'b' and the remainder of 'a' divided by 'b', until 'b' is zero. At that point, 'a' will be the greatest common divisor. 

Note that this script also handles cases where the input values are not integers, as well as cases where the input values are negative. The `abs` function is used to ensure that the GCD is always positive.