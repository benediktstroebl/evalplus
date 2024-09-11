```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to calculate the GCD.
    The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers
    does not change if the larger number is replaced by its difference with the smaller number.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    # Ensure a is greater than or equal to b
    if b > a:
        a, b = b, a  # Swap a and b

    # If b is zero, the GCD is a
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    return a


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function takes two integers `a` and `b` as input, swaps them if necessary to ensure `a` is greater than or equal to `b`, and then enters a loop where it repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` is zero. At this point, `a` is the GCD, which is then returned. The script also includes test cases to demonstrate the function's usage.