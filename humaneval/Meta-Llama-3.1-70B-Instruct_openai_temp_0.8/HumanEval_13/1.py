```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.

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
    # Ensure a is the larger number
    if b > a:
        a, b = b, a
    
    # If b is zero, the GCD is a
    if b == 0:
        return a
    
    # Otherwise, recursively call the function with b and the remainder of a/b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a recursive function `greatest_common_divisor` that uses the Euclidean algorithm to calculate the GCD of two integers `a` and `b`. It also includes test cases to verify its correctness.