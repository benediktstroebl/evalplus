```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # In every step of Euclidean algorithm, divide the larger number by the smaller one
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two numbers that is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. The algorithm continues until the remainder is 0, at which point the non-zero remainder is the GCD of the original two numbers. The `abs` function is used to ensure that the GCD is always positive, even if the input numbers are negative.