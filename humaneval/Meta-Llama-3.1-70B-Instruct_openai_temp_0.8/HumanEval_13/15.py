```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.
    The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """

    # Ensure a is the larger number
    if a < b:
        a, b = b, a  # Swap a and b

    # Replace a with the remainder of a divided by b until b is 0
    while b!= 0:
        a, b = b, a % b  # Swap a and b, and replace b with the remainder of a divided by b

    # At this point, a is the GCD of the original a and b
    return a


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function takes two integers `a` and `b` as input, and returns their greatest common divisor.

The script also includes test cases to verify the correctness of the function. The test cases are based on the examples provided in the problem statement.