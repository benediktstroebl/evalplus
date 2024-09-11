```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The function uses the Euclidean algorithm, which is a way of calculating the greatest common divisor
    of two numbers based on the principle that the greatest common divisor of two numbers does not
    change if the larger number is replaced by its difference with the smaller number.

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
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    # At this point, a is the greatest common divisor
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the greatest common divisor. The script also includes docstrings and test cases to demonstrate the function's correctness.