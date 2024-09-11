```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the greatest common divisor.
    The Euclidean algorithm is a method for computing the greatest common divisor of two numbers,
    based on the principle that the greatest common divisor of two numbers does not change
    if the larger number is replaced by its difference with the smaller number.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b
    """

    # Use the Euclidean algorithm to find the greatest common divisor
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    # Return the greatest common divisor
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Should print 1
print(greatest_common_divisor(25, 15))  # Should print 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to find the greatest common divisor. The script also includes test cases to verify the correctness of the function.