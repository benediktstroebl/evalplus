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
    
    # Ensure a is the larger number
    if b > a:
        a, b = b, a
    
    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b
    
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm, which is an efficient method for computing the greatest common divisor (GCD) of two integers. The algorithm works by repeatedly replacing `(a, b)` with `(b, a % b)` until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`. 

To make the code more readable and maintainable, I have added a docstring to explain the function's purpose, parameters, return value, and examples of use. I have also added comments to explain the algorithm used.