```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    The function uses the Euclidean algorithm to find the greatest common divisor.
    
    Args:
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

    # Use the Euclidean algorithm to find the greatest common divisor
    while b!= 0:
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    
    # When 'b' is zero, 'a' is the greatest common divisor
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that uses the Euclidean algorithm to find the greatest common divisor of two integers `a` and `b`. It then tests the function with two examples. The Euclidean algorithm is a simple and efficient method for finding the greatest common divisor of two integers. It works by replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, repeating this process until `b` is zero. At that point, `a` is the greatest common divisor.