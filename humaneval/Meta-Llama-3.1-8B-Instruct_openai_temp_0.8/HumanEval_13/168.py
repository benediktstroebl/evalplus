```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    Parameters:
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
    
    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    
    # When 'b' is 0, 'a' is the GCD
    return abs(a)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The Euclidean algorithm is an efficient method for calculating the GCD of two numbers, and it works by repeatedly replacing 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b', until 'b' is 0. The GCD is then the last non-zero remainder, which is 'a' at this point. The `abs` function is used to ensure the GCD is always positive.