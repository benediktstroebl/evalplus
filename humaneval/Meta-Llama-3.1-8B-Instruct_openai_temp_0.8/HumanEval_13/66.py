```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    The function calculates the GCD of two numbers using the Euclidean algorithm.
    
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
    # Ensure a is the larger number to simplify the calculation
    if b > a:
        a, b = b, a
    
    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b
    
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that calculates the GCD of two integers `a` and `b` using the Euclidean algorithm. The function ensures that `a` is the larger number, then iteratively replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` becomes 0. The GCD is then returned as the absolute value of `a`. The script includes test cases to verify the correctness of the function.