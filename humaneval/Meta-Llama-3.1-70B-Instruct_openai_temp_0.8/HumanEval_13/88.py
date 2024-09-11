```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD of two numbers.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a is the larger number
    if b > a:
        a, b = b, a

    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b

    return a


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The function swaps `a` and `b` if `b` is larger, and then enters a loop where it repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` is zero. At this point, `a` is the GCD of the original `a` and `b`. The function returns this value.

The script also includes a test suite in the form of a `if __name__ == "__main__":` block, which prints the results of calling `greatest_common_divisor` with the example inputs `(3, 5)` and `(25, 15)`.