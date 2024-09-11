```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD of two integers.
    The Euclidean algorithm is a method for finding the greatest common divisor (GCD) of two numbers.
    It works by repeatedly applying the division algorithm, swapping the remainder with the divisor, until the remainder is zero.
    The last non-zero remainder is the GCD.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """

    # Handle the edge case where a is zero
    if a == 0:
        return b

    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b

    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script implements the `greatest_common_divisor` function using the Euclidean algorithm to find the GCD of two integers. The function takes two integers `a` and `b` as input and returns their GCD. The test cases at the end of the script demonstrate how to use the function.