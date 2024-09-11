```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Example use cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(48, 18))  # Output: 6
```

This script defines a `greatest_common_divisor` function that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which is an efficient method for calculating the GCD. The algorithm repeatedly replaces `a` and `b` with `b` and `a % b` until `b` is zero, at which point `a` is the GCD.

The script also includes example use cases in the `if __name__ == "__main__":` block, which demonstrate how to use the `greatest_common_divisor` function.