### Greatest Common Divisor (GCD) in Python

The following Python function uses the Euclidean algorithm to find the greatest common divisor of two integers.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD.

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
        # In each step, the remainder of the division of a by b is stored in a
        # and b is updated to be the previous b
        a, b = b, a % b
    return a

# Example usage:
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This function works by repeatedly replacing `a` and `b` with `b` and `a mod b`, respectively, until `b` is zero. At this point, `a` is the greatest common divisor of the original `a` and `b`.