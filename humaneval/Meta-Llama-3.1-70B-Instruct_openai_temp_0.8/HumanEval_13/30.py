```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to calculate the GCD.
    The Euclidean algorithm is a method for finding the greatest common divisor of two numbers,
    a and b, by repeatedly applying the division algorithm.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """

    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)

    # If b is zero, the GCD is a
    if b == 0:
        return a

    # Otherwise, the GCD of a and b is the same as the GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a recursive function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input, ensures they are positive, and then applies the Euclidean algorithm to calculate their GCD. The script also includes test cases to verify the correctness of the function.