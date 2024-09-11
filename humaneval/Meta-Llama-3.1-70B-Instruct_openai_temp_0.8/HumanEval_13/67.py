```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
print(greatest_common_divisor(48, 18))  # Expected output: 6
print(greatest_common_divisor(101, 103))  # Expected output: 1
```

In this script, the `greatest_common_divisor` function takes two integers `a` and `b` and returns their greatest common divisor. It uses the Euclidean algorithm to achieve this. The algorithm works by repeatedly applying the division algorithm, swapping the remainder with the divisor, until the remainder is 0. The GCD is then the last non-zero remainder.

The script includes test cases to verify the correctness of the function.