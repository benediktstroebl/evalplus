### Greatest Common Divisor (GCD) Calculation
#### Using Euclidean Algorithm

The Euclidean algorithm is an efficient method for calculating the greatest common divisor (GCD) of two integers.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    The Euclidean algorithm is used to find the GCD.
    
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
    while b!= 0:
        # Swap the values of a and b
        a, b = b, a % b
    
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the GCD of two integers. The algorithm works by repeatedly replacing 'a' and 'b' with 'b' and the remainder of 'a' divided by 'b', until 'b' is zero. At this point, 'a' is the GCD. The function also handles negative inputs by taking the absolute value of the result.