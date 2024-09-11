```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

In this script, I've implemented the greatest common divisor function using the Euclidean algorithm, which is an efficient method for computing the GCD of two integers. The function takes two integers `a` and `b` as input, and returns their greatest common divisor. The function uses the remainder operator (`%`) to repeatedly replace `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` becomes zero. At that point, `a` will be the greatest common divisor. The `abs` function is used to ensure that the GCD is always positive, as the GCD is a measure of similarity between two numbers and is therefore always non-negative.