```python
# Define a function to calculate the greatest common divisor of two integers
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm to efficiently calculate the GCD.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Ensure a is the larger number to simplify the loop
    if b > a:
        a, b = b, a
    
    # Use the Euclidean algorithm to calculate the GCD
    while b!= 0:
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    
    # At this point, 'a' is the GCD
    return a

# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```