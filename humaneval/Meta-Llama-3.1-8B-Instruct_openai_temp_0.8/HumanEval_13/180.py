```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b
    using the Euclidean algorithm.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
print(greatest_common_divisor(12, 8))  # Expected output: 4
print(greatest_common_divisor(-12, 8))  # Expected output: 4
print(greatest_common_divisor(0, 10))  # Expected output: 10
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The GCD is the largest number that divides both numbers without leaving a remainder. The Euclidean algorithm is a simple and efficient method for calculating the GCD of two numbers. 

The function `greatest_common_divisor` takes two integers `a` and `b` as input and returns their GCD. It uses a while loop to repeatedly replace `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` becomes zero. At this point, `a` is the GCD of the original `a` and `b`. The `abs` function is used to ensure that the result is always positive, even if the input numbers have different signs.