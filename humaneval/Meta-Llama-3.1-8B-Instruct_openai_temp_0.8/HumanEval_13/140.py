```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    Parameters:
    a (int): The first integer
    b (int): The second integer
    
    Returns:
    int: The greatest common divisor of a and b
    """
    
    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    
    # At this point, 'a' is the GCD
    return abs(a)


# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
    print(greatest_common_divisor(48, 18))  # Expected output: 6
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The GCD is the largest positive integer that divides both numbers without leaving a remainder. The algorithm works by repeatedly replacing 'a' and 'b' with 'b' and the remainder of 'a' divided by 'b', respectively. This process continues until 'b' is 0, at which point 'a' is the GCD. The absolute value of the GCD is returned to ensure that the result is always positive.