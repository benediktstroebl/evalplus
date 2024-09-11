```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    The algorithm used is the Euclidean algorithm, which is a popular method for computing the GCD of two numbers.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b
    """
    while b!= 0:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The algorithm works by repeatedly replacing (a, b) with (b, a % b) until b is 0, at which point a is the greatest common divisor of the original a and b.