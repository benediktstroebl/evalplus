```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b

    The function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers
    does not change if the larger number is replaced by its difference with the smaller number.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b!= 0:
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    return abs(a)  # Return the absolute value of the GCD

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). The GCD is calculated using the Euclidean algorithm, which iteratively replaces the larger number with its difference with the smaller number until the two numbers are equal. The function then returns the absolute value of this equal number, which is the GCD. The script also includes test cases to demonstrate the function's correctness.