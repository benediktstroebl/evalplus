```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method 
    for computing the greatest common divisor (GCD) of two integers.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap the values of a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` is zero, at which point `a` is the greatest common divisor. The script also includes test cases to verify the correctness of the function.