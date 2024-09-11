```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is a way of calculating the greatest common divisor of two numbers,
    a and b, by repeatedly applying the division algorithm.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```
In this script, the `greatest_common_divisor` function takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which repeatedly replaces `a` and `b` with `b` and `a % b` until `b` is 0. At this point, `a` is the greatest common divisor of the original `a` and `b`. The script also includes two test cases to verify the function's correctness.