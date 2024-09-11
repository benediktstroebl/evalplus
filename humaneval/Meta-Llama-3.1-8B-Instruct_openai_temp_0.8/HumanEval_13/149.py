```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers is the largest positive integer that divides each of the integers without a remainder.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    
    # Use the Euclidean algorithm to find the GCD of a and b
    while b:
        # In each iteration, replace a with b and b with the remainder of a divided by b
        a, b = b, a % b
    
    # After the loop ends, a will be the GCD of the original a and b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. It then tests the function with the provided test cases. The `abs` function is used to ensure the GCD is always positive, even if the input integers have different signs.