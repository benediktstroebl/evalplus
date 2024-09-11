```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm, which is an efficient method for computing the greatest common divisor of two integers.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines the `greatest_common_divisor` function, which takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which repeatedly replaces `a` and `b` with `b` and `a % b` until `b` is zero. At this point, `a` is the greatest common divisor.

The script also includes two test cases to demonstrate the function's correctness.