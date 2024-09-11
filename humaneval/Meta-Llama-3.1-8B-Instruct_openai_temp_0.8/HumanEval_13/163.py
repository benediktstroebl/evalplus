```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The function uses the Euclidean algorithm, which is an efficient method 
    for computing the greatest common divisor of two integers.

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
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The GCD is the largest positive integer that divides both `a` and `b` without leaving a remainder.

The function works by repeatedly swapping `a` and `b`, and replacing `b` with the remainder of `a` divided by `b`. This process continues until `b` is zero, at which point `a` is the GCD.

The script includes two test cases to verify the correctness of the function. When run, it prints the GCD of 3 and 5, and the GCD of 25 and 15.