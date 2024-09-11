```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the greatest common divisor.

    Parameters:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b
    """
    # Ensure a is the larger number
    if b > a:
        a, b = b, a
    
    # If b is zero, the greatest common divisor is a
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b
    
    # At this point, b is zero and a is the greatest common divisor
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```