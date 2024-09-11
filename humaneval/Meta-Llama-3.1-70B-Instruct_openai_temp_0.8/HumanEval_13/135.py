```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm to find the GCD of two numbers.
    
    Args:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a
    
    # Continue to divide the larger number by the smaller number until the remainder is 0
    while b!= 0:
        # Store the remainder of the division
        remainder = a % b
        # Update the larger number to be the smaller number and vice versa
        a, b = b, remainder
    
    # The GCD is the last non-zero remainder
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```