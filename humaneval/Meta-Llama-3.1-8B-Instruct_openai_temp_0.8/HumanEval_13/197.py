```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b

    The Euclidean algorithm is used to calculate the greatest common divisor.
    This algorithm is based on the principle that the greatest common divisor
    of two numbers does not change if the larger number is replaced by its
    difference with the smaller number.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b
    """
    # Ensure a is the larger number
    if b > a:
        a, b = b, a

    # Use the Euclidean algorithm to calculate the greatest common divisor
    while b!= 0:
        a, b = b, a % b

    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function then tests this function with the provided example use cases.