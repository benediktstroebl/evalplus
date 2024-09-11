### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

Below is a Python script that implements the Euclidean algorithm to find the greatest common divisor (GCD) of two integers.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)


# Example usage:
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm, which is a well-known method for calculating the GCD. It repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` is zero. At this point, `a` is the GCD of the original `a` and `b`. The `abs` function is used to ensure the result is always positive.