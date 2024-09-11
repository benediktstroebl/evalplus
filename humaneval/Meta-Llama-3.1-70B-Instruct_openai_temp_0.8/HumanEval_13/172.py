```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which is a well-known method for calculating the GCD of two numbers.

The script also includes two test cases to demonstrate the function's correctness. The `abs` function is used to ensure the GCD is always non-negative, as the GCD is defined to be positive.