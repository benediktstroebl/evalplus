### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers is the largest positive integer that divides both numbers without leaving a remainder.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    while b:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return a

# Example use cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script implements the Euclidean algorithm to find the greatest common divisor of two integers. The Euclidean algorithm is a simple and efficient method for computing the GCD of two numbers. It works by repeatedly applying the division algorithm, swapping the dividend and remainder, until the remainder is zero. The GCD is then the last non-zero remainder.