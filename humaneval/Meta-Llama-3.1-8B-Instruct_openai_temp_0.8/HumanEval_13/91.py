### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD of two numbers.
    This algorithm works by repeatedly applying the division algorithm,
    swapping the remainder with the divisor, until the remainder is zero.

    :param a: First integer
    :param b: Second integer
    :return: Greatest common divisor of a and b
    """
    # Ensure a and b are positive
    a, b = abs(a), abs(b)

    # If b is zero, the remainder is a, so return a
    while b:
        a, b = b, a % b

    return a

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(48, 18))  # Output: 6
```

This script calculates the GCD of two integers `a` and `b` using the Euclidean algorithm. This algorithm is a simple and efficient method for computing the GCD of two numbers.