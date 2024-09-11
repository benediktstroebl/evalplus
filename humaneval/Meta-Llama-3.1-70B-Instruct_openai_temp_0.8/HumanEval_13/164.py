```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

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

    # Ensure a and b are non-negative
    a = abs(a)
    b = abs(b)

    # If b is zero, the GCD is a
    if b == 0:
        return a

    # Otherwise, recursively call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines the `greatest_common_divisor` function, which calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The function is then tested with two example cases. The `if __name__ == "__main__":` block ensures that the tests are only run when the script is executed directly, not when it's imported as a module.