### Greatest Common Divisor (GCD) in Python
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is a simple and efficient method for computing the GCD of two numbers.

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

    # Ensure a is the larger number
    if b > a:
        a, b = b, a

    # Use the Euclidean algorithm
    while b!= 0:
        a, b = b, a % b

    return abs(a)


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function is well-documented with a docstring that explains how it works and includes example use cases. The script also includes some example usage of the function to demonstrate its correctness.