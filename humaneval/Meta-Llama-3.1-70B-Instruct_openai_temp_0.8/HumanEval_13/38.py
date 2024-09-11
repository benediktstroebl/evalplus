```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`. The function returns the absolute value of `a` to ensure the result is always non-negative. The script also includes two test cases to demonstrate the function's behavior.