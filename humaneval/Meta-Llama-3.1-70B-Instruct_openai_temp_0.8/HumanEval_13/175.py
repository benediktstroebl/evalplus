```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm, which is an efficient method 
    for computing the greatest common divisor of two numbers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    # Ensure a is the larger number to simplify the loop
    if b > a:
        a, b = b, a
    
    # Continue to divide a by b until b is 0
    while b!= 0:
        # a becomes b and b becomes the remainder of a divided by b
        a, b = b, a % b
    
    # a is now the greatest common divisor
    return a

# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Expected output: 1
    print(greatest_common_divisor(25, 15)) # Expected output: 5
```

This script defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input, ensures that `a` is the larger number, and then repeatedly divides `a` by `b` until `b` is 0. At this point, `a` is the GCD of the original `a` and `b`. The function includes docstrings and example use cases to demonstrate its usage. The script also includes test cases to verify its correctness.