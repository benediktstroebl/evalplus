```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm to find the GCD.
    
    Args:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)
    
    # If b is zero, the GCD is a
    while b!= 0:
        # Otherwise, replace a with b and b with the remainder of a divided by b
        a, b = b, a % b
    
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
print(greatest_common_divisor(48, 18))  # Expected output: 6
print(greatest_common_divisor(101, 103))  # Expected output: 1
```