```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is a way to find the greatest common divisor of two numbers,
    a and b, by repeatedly applying the division algorithm.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Example use cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(48, 18))  # Output: 6
print(greatest_common_divisor(101, 103))  # Output: 1
```

This script defines the `greatest_common_divisor` function, which takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which is a simple and efficient way to find the GCD of two numbers.

The script also includes some example use cases to demonstrate how to use the `greatest_common_divisor` function.