```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b
    """
    # Use the Euclidean algorithm to compute the GCD
    while b:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two numbers by repeatedly applying the identity gcd(a, b) = gcd(b, a % b) until b is zero. At this point, a is the GCD of the original a and b. The `abs` function is used to ensure the GCD is always positive, even if the input numbers are negative.