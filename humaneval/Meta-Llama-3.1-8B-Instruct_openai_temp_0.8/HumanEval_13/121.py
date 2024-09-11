```python
# greatest_common_divisor.py

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD of two numbers.
    The Euclidean algorithm is a method for computing the greatest common divisor (GCD) of two numbers,
    based on the principle that the greatest common divisor of two numbers does not change if the larger
    number is replaced by its difference with the smaller number.

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

    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b

    return a


# Example usage:
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD. The script also includes example usage in the `if __name__ == "__main__":` block.