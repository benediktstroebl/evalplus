```python
def greatest_common_divisor(a: int, b: int) -> int:
    """Return a greatest common divisor of two integers a and b
    
    This function uses the Euclidean algorithm to calculate the GCD.
    
    Args:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The greatest common divisor of a and b.
    
    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap a and b
        a, b = b, a % b
    return abs(a)

# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected: 1
    print(greatest_common_divisor(25, 15))  # Expected: 5
    print(greatest_common_divisor(48, 18))  # Expected: 6
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. It repeatedly replaces `b` with the remainder of `a` divided by `b` until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`. The script also includes some test cases to demonstrate its usage.