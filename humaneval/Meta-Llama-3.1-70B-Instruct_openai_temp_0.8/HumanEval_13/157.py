```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers.
    The algorithm works by repeatedly applying the division algorithm, swapping the remainder with the divisor,
    until the remainder is zero. At that point, the non-zero remainder is the GCD.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Test cases
if __name__ == "__main__":
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(101, 103) == 1
```

This script defines the `greatest_common_divisor` function, which calculates the GCD of two integers using the Euclidean algorithm. The function takes two integers as input and returns their GCD.

The script also includes test cases to verify the correctness of the `greatest_common_divisor` function. These test cases are executed when the script is run directly (i.e., not when it's imported as a module by another script).

Note: The `abs` function is used to ensure the result is always non-negative, even if the input values are negative.