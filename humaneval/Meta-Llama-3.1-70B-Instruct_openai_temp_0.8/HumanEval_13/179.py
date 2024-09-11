```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two integers.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The greatest common divisor of a and b.
    """
    while b!= 0:
        # Swap the values of a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```