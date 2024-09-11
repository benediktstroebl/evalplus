```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    The greatest common divisor (GCD) of two integers a and b, denoted as GCD(a, b),
    is the largest positive integer that divides both a and b without leaving a remainder.
    
    :param a: The first integer
    :param b: The second integer
    :return: The GCD of a and b
    """
    
    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a
    
    # Recursive case: Replace (a, b) with (b, a % b)
    # until b is zero
    else:
        # Calculate the remainder of a divided by b
        remainder = a % b
        
        # Recursive call with b and remainder
        return greatest_common_divisor(b, remainder)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The algorithm works by recursively replacing `(a, b)` with `(b, a % b)` until `b` is zero, at which point the GCD is `a`.