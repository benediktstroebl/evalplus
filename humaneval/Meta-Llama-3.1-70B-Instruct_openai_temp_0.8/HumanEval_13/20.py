```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)
    
    # If b is zero, the GCD is a
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b
    
    # At this point, b is zero, so a is the GCD
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

In this script, the `greatest_common_divisor` function uses the Euclidean algorithm to find the greatest common divisor of two integers `a` and `b`. The algorithm works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At this point, `a` is the greatest common divisor.

The script includes test cases to verify that the function is working correctly. The expected output of each test case is provided in a comment.