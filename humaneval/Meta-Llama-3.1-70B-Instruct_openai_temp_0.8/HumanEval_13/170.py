```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.
    
    This function uses the Euclidean algorithm to find the greatest common divisor.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b`. It uses the Euclidean algorithm, which repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD.

The script also includes two test cases to verify the correctness of the function. The tests check that the GCD of 3 and 5 is 1, and the GCD of 25 and 15 is 5.