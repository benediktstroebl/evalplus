```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    The function uses the Euclidean algorithm to find the greatest common divisor.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    
    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # If b is zero, the greatest common divisor is a
    if b == 0:
        return a
    
    # Otherwise, recursively call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the greatest common divisor. If `b` is zero, the function returns `a`. Otherwise, it recursively calls itself with `b` and the remainder of `a` divided by `b`. The script then tests the function with the provided examples.