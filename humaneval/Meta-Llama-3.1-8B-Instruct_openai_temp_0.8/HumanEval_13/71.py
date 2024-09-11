```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b

    The greatest common divisor (GCD) of two integers a and b is the largest number that divides both a and b without leaving a remainder.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The Euclidean algorithm works by repeatedly applying the division algorithm, swapping the remainder with the divisor, until the remainder is zero. At that point, the non-zero remainder is the greatest common divisor of the original two numbers.