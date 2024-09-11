```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    This function returns the greatest common divisor of two integers a and b.
    
    The greatest common divisor (GCD) of two integers a and b is the largest positive integer that divides each of the integers without a remainder.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    
    # Ensure that a is the larger number
    if b > a:
        a, b = b, a
    
    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b
    
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the GCD of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two numbers and is based on the principle that the GCD of two numbers does not change if the larger number is replaced by its difference with the smaller number. This is repeated until the two numbers become equal, at which point the GCD is the last non-zero remainder. The absolute value is used to ensure a positive result.