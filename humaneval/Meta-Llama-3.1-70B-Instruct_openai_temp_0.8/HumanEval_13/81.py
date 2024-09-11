```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm to compute the GCD.
    
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
        # In each iteration, we replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'.
        # This is based on the property that the GCD of 'a' and 'b' is the same as the GCD of 'b' and the remainder of 'a' divided by 'b'.
        a, b = b, a % b
    
    # When 'b' becomes zero, 'a' is the GCD.
    return a

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```