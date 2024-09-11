```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b

    Args:
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
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The Euclidean algorithm is a simple method for computing the GCD of two numbers, and it works by successively replacing 'a' and 'b' with 'b' and the remainder of 'a' divided by 'b' until 'b' is zero. At that point, 'a' is the GCD of the original 'a' and 'b'.