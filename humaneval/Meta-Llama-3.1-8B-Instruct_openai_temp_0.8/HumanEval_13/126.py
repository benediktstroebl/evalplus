```python
# Calculate the Greatest Common Divisor (GCD) of two integers
# This script uses the Euclidean algorithm to efficiently compute GCD

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    Args:
        a (int): The first integer
        b (int): The second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    
    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a
    
    # Recursive case: The GCD of a and b is the same as the GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to calculate the GCD of two integers. It uses recursion to efficiently compute the GCD. If `b` is zero, the GCD is `a`. Otherwise, the GCD is the same as the GCD of `b` and the remainder of `a` divided by `b`.